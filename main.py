import streamlit as st
import plotly.express as px
from backend import get_data

#add title, text input, selectbox and subheader

st.title("Weather forecast for the next days")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days for the weather forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        #get the temperature or sky data 
        filtered_data = get_data(place, days)

        if option == "Temperature":

            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data] # main is the dictionary and temp is a key in dictionary list
           
            dates = [dict["dt_txt"] for dict in filtered_data]
           
            #create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})   # Create a simple line chart using Plotly Express
            #adding a graphic
            st.plotly_chart(figure)

        else:
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            #"Clear" is a key from dictionary of weather and it refers to sky
           
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data] #weather is the dictionary and main is key in dictionary list
            #[0] extracts the dictionary because is one single dictionary in this weather list -> weather:[{'': '', '': '', '': ''}]
            
            image_paths = [images[condition] for condition in sky_conditions]

            #displays date and time below every image
            dates = [dict["dt_txt"] for dict in filtered_data]
            for img, date in zip(image_paths, dates):
                st.image(img, width=115, caption=date)
                
    except KeyError: 
        st.write("That place does not exist")