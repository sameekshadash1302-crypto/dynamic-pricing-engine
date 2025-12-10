import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("demand_model.pkl")

# We will simulate prices from ₹100 to ₹1500
test_prices = np.arange(100, 1501, 20)

# Fix other conditions (average scenario)
competitor_price = 900
promo = 0
day_of_week = 3   # mid-week
base_price = 700

results = []

for price in test_prices:
    X = [[price, competitor_price, promo, day_of_week, base_price]]
    predicted_units = model.predict(X)[0]

    revenue = price * predicted_units

    results.append([price, predicted_units, revenue])

df_sim = pd.DataFrame(results, columns=["price", "predicted_units", "predicted_revenue"])

# Find best price
best_row = df_sim.loc[df_sim["predicted_revenue"].idxmax()]

print("🏆 BEST PRICE FOUND")
print("Price:", round(best_row["price"], 2))
print("Predicted Units Sold:", round(best_row["predicted_units"], 2))
print("Predicted Revenue:", round(best_row["predicted_revenue"], 2))

# Plot the curve
plt.plot(df_sim["price"], df_sim["predicted_revenue"])
plt.xlabel("Price")
plt.ylabel("Predicted Revenue")
plt.title("Price vs Predicted Revenue")
plt.show()