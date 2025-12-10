# src/train_demand_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
df = pd.read_csv("data/pricing_data.csv")

# Define features (X) and target (y)
X = df[[
    "price",
    "competitor_price",
    "promo",
    "day_of_week",
    "base_price"
]]

y = df["units_sold"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("🎯 Model Evaluation")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 3))

# Save the model
joblib.dump(model, "demand_model.pkl")
print("✅ Model saved as demand_model.pkl")

import joblib

model = joblib.load("demand_model.pkl")

print("Predicted units sold:", 
      model.predict([[500, 600, 0, 3, 700]])[0])
