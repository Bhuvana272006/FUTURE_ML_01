import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Sales Forecasting App")

date = st.date_input("Select Order Date")
quantity = st.number_input("Quantity")
discount = st.number_input("Discount")
profit = st.number_input("Profit")

year = date.year
month = date.month
day = date.day
day_of_week = date.weekday()
is_weekend = 1 if day_of_week >= 5 else 0
quarter = (month - 1) // 3 + 1

if st.button("Predict"):
    input_data = [[quantity, discount, profit,
                   year, month, day, day_of_week, is_weekend, quarter]]
    
    prediction = model.predict(input_data)
    st.write("Predicted Sales:", prediction[0])
