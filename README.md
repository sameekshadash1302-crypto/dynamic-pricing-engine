code README.md
Dynamic Pricing Engine — Machine Learning + Business Optimization
An end-to-end pricing optimization system that predicts demand, simulates revenue at different price points, and recommends the best price to maximize earnings.
🚀 Built with
Python
Pandas
NumPy
Scikit-Learn
Streamlit
Matplotlib
dynamic_pricing_project/
│
├── data/                    # Synthetic pricing dataset
├── src/
│   ├── generate_pricing_data.py     # Day 2
│   ├── train_demand_model.py        # Day 3
│   ├── revenue_simulation_day4.py   # Day 4
│   └── pricing_decision_engine_day5.py
│
├── app_pricing_dashboard_day8.py    # Final dashboard
└── README.md
📊 What This Engine Does
✔ Predicts demand
Uses a trained Random Forest model to estimate units sold for any price.
✔ Simulates 100+ price points
Generates a Price vs Revenue curve to find the best price.
✔ Recommends action
Increase price
Decrease price
Hold price
based on expected revenue gain.
✔ Interactive Streamlit Dashboard
Includes:
Input sidebar
Best price recommendation
KPI cards
Price scenario table
Revenue curve
Demand curve
🧠 How Pricing Optimization Works (Simple Explanation)
Lower price → more demand
Higher price → fewer units
Revenue depends on BOTH
Our engine tries many prices, predicts demand, and finds where revenue is maximum.
This is exactly how airlines, Uber, ecommerce, and food delivery apps price products.
