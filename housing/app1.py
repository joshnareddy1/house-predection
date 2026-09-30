import streamlit as st
import joblib

model = joblib.load("model_trained.pk2")

st.title("🏠 House Price Prediction")
st.write("My House Price Prediction Project using Streamlit")
avg_area_income = st.number_input("Enter Average Area Income",min_value=0.0)
avg_area_house_age = st.number_input("Enter Average Area House Age", min_value=0.0)
avg_area_number_of_rooms = st.number_input("Enter Average Area Number of Rooms",min_value=0.0)
avg_area_number_of_bedrooms = st.number_input("Enter Average Area Number of Bedrooms",min_value=0.0)
area_population = st.number_input("Enter Area Population",min_value=0.0)

if st.button("Predict House Price"):

    input_list = [[
        avg_area_income,
        avg_area_house_age,
        avg_area_number_of_rooms,
        avg_area_number_of_bedrooms,
        area_population
    ]]

    predicted_price = model.predict(input_list)

    st.success(
        f"Predicted House Price: {predicted_price[0]:,.2f}"
    )