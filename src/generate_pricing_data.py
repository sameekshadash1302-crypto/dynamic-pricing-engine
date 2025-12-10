# src/generate_pricing_data.py
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

n_products = 10            # number of distinct products
days = 200                # number of days (time series length)
rows = n_products * days

product_ids = np.repeat(np.arange(1, n_products+1), days)

# base price per product (random but stable per product)
base_prices = np.round(np.repeat(np.random.uniform(150, 1200, size=n_products), days), 2)

# competitor price (base +/- small noise)
competitor_price = np.round(base_prices * np.random.uniform(0.9, 1.15, size=rows), 2)

# promotional flag randomly (10% chance)
promo_flag = np.random.binomial(1, 0.10, size=rows)

# seasonality: weekday effect (0..6)
day_of_week = np.tile(np.arange(0, 7), int(np.ceil(rows/7)))[:rows]

# price we set: sometimes we discount for promo, sometimes slightly change around base
price = np.round(base_prices * np.where(promo_flag==1, np.random.uniform(0.75, 0.95, size=rows),
                                        np.random.uniform(0.9, 1.1, size=rows)), 2)

# demand generation using a simple price-elastic function + noise
# baseline demand per product
baseline_demand_per_product = np.repeat(np.random.uniform(20, 120, size=n_products), days)

# price elasticity: negative values, larger magnitude = more sensitive
elasticity_per_product = np.repeat(np.random.uniform(-1.5, -0.3, size=n_products), days)

# competitor effect: if competitor is cheaper, reduce demand; if competitor is higher, increase demand slightly
comp_diff = (competitor_price - price) / competitor_price  # positive if competitor is more expensive

# promo multiplier and weekday multiplier
promo_mult = 1 + 0.6 * promo_flag
weekday_mult = 1 + 0.1 * ((day_of_week == 5) | (day_of_week == 6))  # weekends +10%

# units sold (ensure positive & integer)
units_sold_cont = baseline_demand_per_product * (price / base_prices) ** elasticity_per_product
units_sold = (units_sold_cont * promo_mult * (1 + comp_diff) * weekday_mult + np.random.normal(0, 3, size=rows)).clip(min=0)
units_sold = np.round(units_sold).astype(int)

# cost per unit (random fraction of base price)
cost = np.round(base_prices * np.random.uniform(0.35, 0.6, size=rows), 2)

revenue = np.round(price * units_sold, 2)
profit = np.round((price - cost) * units_sold, 2)

df = pd.DataFrame({
    "product_id": product_ids,
    "day": np.tile(np.arange(1, days+1), n_products),
    "base_price": base_prices,
    "price": price,
    "competitor_price": competitor_price,
    "promo": promo_flag,
    "day_of_week": day_of_week,
    "units_sold": units_sold,
    "cost_per_unit": cost,
    "revenue": revenue,
    "profit": profit
})

out = Path("data/pricing_data.csv")
out.parent.mkdir(exist_ok=True)
df.to_csv(out, index=False)

print("✅ Created synthetic pricing data:", out, "with rows =", len(df))
