import streamlit as st
import plotly.express as px
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of weather forecast days.")
option = st.selectbox("Select data to view", ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2023-22-1", "2023-23-2", "2023-24-3"]
    temperatures = [10, 15, 16]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (c)"})
st.plotly_chart(figure)