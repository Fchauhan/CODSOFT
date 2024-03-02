import tkinter as tk

import requests

 

def get_weather():

    city = city_entry.get()

    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b9821a4b7c46c98de4ebb57990dd8098&units=metric"

    response = requests.get(url)

    weather_data = response.json()

 

    if weather_data['cod'] != '404':

        temperature = weather_data['main']['temp']

        humidity = weather_data['main']['humidity']

        description = weather_data['weather'][0]['description']

        weather_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")

    else:

        weather_label.config(text="City not found")

 

# Create the main window

window = tk.Tk()

window.title("Weather Forecast App")

 

# Create and place widgets

city_label = tk.Label(window, text="Enter city:")

city_label.pack()

 

city_entry = tk.Entry(window)

city_entry.pack()

 

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)

get_weather_button.pack()

 

weather_label = tk.Label(window, text="")

weather_label.pack()

 

# Run the application

window.mainloop()

