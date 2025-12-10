import numpy as np
import joblib

# Load trained demand model
model = joblib.load("demand_model.pkl")

# ----- CURRENT MARKET SITUATION (You can change these later) -----
current_price = 800
competitor_price = 780
promo = 0
day_of_week = 4
base_price = 700

# Try small price changes: -20%, -10%, 0%, +10%, +20%
price_changes = [-0.2, -0.1, 0.0, 0.1, 0.2]

results = []

for change in price_changes:
    test_price = current_price * (1 + change)

    X = [[test_price, competitor_price, promo, day_of_week, base_price]]
    predicted_units = model.predict(X)[0]

    predicted_revenue = test_price * predicted_units

    results.append([round(test_price, 2), round(predicted_units, 2), round(predicted_revenue, 2)])

# Print comparison table
print("\n📊 PRICE CHANGE COMPARISON\n")
print("Price | Units Sold | Revenue")
print("-" * 30)

for r in results:
    print(r[0], "|", r[1], "|", r[2])

# Find best option
best_option = max(results, key=lambda x: x[2])

print("\n🏆 BEST DECISION")
print("Best Price:", best_option[0])
print("Expected Units Sold:", best_option[1])
print("Expected Revenue:", best_option[2])

# Human-like recommendation
if best_option[0] > current_price:
    print("✅ Recommendation: INCREASE price")
elif best_option[0] < current_price:
    print("⚠️ Recommendation: DECREASE price")
else:
    print("😴 Recommendation: KEEP price same")
