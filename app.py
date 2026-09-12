import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("Weather_API_KEY")  # Retrieve API key from environment variables
st.set_page_config(page_title="Weather App", page_icon="🌞")
st.title("Weather App!")
st.write("Enter a city name and click 'Get Weather' to get the current weather information.")
city = st.text_input("Enter City Name:")

API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" #constants and unique variable are written in capital letters

if st.button("Get Weather"): #when button is clicked, the following code will be executed
        response = requests.get(API_URL) #if it is valid city name, the api key will be used to get the weather information

        if response.status_code ==200: #if the response is successful, the following code will be executed
                st.success("Weather data fetched successfully!") 
                data = response.json() #the data will be converted to json format

                #Fetch weather information in variables from the API response
                Temperature = data["main"]["temp"] #the temperature will be printed in the console
                Humidity = data["main"]["humidity"] #the humidity will be printed in the console
                Wind_Speed = data["wind"]["speed"] #the wind speed will be printed in the console
                Weather =data["weather"][0]["main"] #here [{}] is there so first we need to go to first dic thus 0 then the variable to fetch

                col1, col2 = st.columns(2) #the columns will be created to display the weather information in a structured format
                col3, col4 = st.columns(2)

                col1.metric("Temperature",f"🌡️{Temperature}°C")
                col2.metric("Humidity",f"💧{Humidity}%")
                col3.metric("Wind Speed",f"💨{Wind_Speed} m/s")     
                col4.metric("Weather",f"⛅{Weather}")
        else:
                st.error("Error: Unable to fetch weather data. Please check the city name and try again.") 
