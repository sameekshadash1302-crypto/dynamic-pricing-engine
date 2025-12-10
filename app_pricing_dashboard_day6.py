import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Dynamic Pricing Engine", page_icon="💸")

st.title("💸 Dynamic Pricing Decision Engine")
st.write("Enter market conditions and get the best price recommendation.")

# Load demand model
model = joblib.load("demand_model.pkl")

st.sidebar.header("📥 Enter Market Values")

current_price = st.sidebar.number_input("Current Price (₹)", 100, 2000, 800)
competitor_price = st.sidebar.number_input("Competitor Price (₹)", 100, 2000, 780)
promo = st.sidebar.selectbox("Promotion Active?", [0, 1])
day_of_week = st.sidebar.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 3)
base_price = st.sidebar.number_input("Base Price (₹)", 100, 2000, 700)

if st.sidebar.button("🧠 Get Pricing Recommendation"):

    price_changes = [-0.2, -0.1, 0.0, 0.1, 0.2]
    results = []

    for change in price_changes:
        test_price = current_price * (1 + change)

        X = [[test_price, competitor_price, promo, day_of_week, base_price]]
        predicted_units = model.predict(X)[0]

        predicted_revenue = test_price * predicted_units

        results.append([round(test_price, 2), round(predicted_units, 2), round(predicted_revenue, 2)])

    st.subheader("📊 Price Scenario Comparison")
    st.table(results)

    best_option = max(results, key=lambda x: x[2])

    st.subheader("🏆 Best Pricing Decision")

    st.metric("Best Price (₹)", best_option[0])
    st.metric("Expected Units Sold", best_option[1])
    st.metric("Expected Revenue (₹)", best_option[2])

    if best_option[0] > current_price:
        st.success("✅ Recommendation: INCREASE the price")
    elif best_option[0] < current_price:
        st.warning("⚠️ Recommendation: DECREASE the price")
    else:
        st.info("😴 Recommendation: KEEP the price same")
