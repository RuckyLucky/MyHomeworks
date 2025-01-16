
import requests
from tkinter import *

# Константы
API_KEY = 'ваш_ключ_API'  # Замените на ваш ключ API
CITY = "Тверь"

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def format_weather_message(weather_dict):
    temp = weather_dict['main']['temp']
    weather = weather_dict['weather'][0]['description']

    message = f"{city}: {weather}, температура: {temp}°C"
    return message

def notify_weather(message):
    print(message)

def main():
    root = Tk()
 
    label = Label(root, text="Введите город:")
    entry = Entry(root)
 
    button = Button(root, text="Получить погоду", command=lambda: display_weather(entry.get()))
 
    label.pack()
    entry.pack()
    button.pack()
 
    root.mainloop()

def display_weather(city):
    weather_data = get_weather(CITY, API_KEY)
    formatted_message = format_weather_message(weather_data)
    notify_weather(formatted_message)

if __name__ == "__main__":
    main()
