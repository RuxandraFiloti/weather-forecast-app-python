import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days for the weather forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

#plot data dynamically -> get_data function takes the data from api
d, t = get_data(place, days, option)


figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})   # Create a simple line chart using Plotly Express

#adding a graphic
st.plotly_chart(figure)
