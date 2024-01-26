import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of weather forecast days.")
option = st.selectbox("Select data to view", ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


try:
    if place:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [data["main"]["temp"] - 273.15 for data in filtered_data]
            dates = [data["dt_txt"] for data in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (c)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_condition = [data["weather"][0]["main"] for data in filtered_data]
            path = [f"images/{sky.lower()}.png" for sky in sky_condition]
            st.image(path, width=115)
except KeyError:
    st.info("Please enter a valid place")


