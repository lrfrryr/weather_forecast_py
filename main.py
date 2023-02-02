import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast")
place = st.text_input("Place:")
days = st.slider("Forecast days:", min_value=1, max_value=5,
                 help="Select the number of forecast days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day(s) in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = [temperature/10 for temperature in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # create a temperature plot
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Day", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            print(type(dates[0]))
            sky_images = {"Clear": "images/sun.png",
                          "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png",
                          "Snow": "images/snow.png"}
            # translate the data
            images_list = [sky_images[condition] for condition in sky_conditions]
            st.image(images_list, caption=dates, width=100)
    except KeyError:
        st.write("That place does not exist! Try again.")



