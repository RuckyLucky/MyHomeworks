
import requests
from plyer import notification

# Константы
API_KEY = "23496c2a58b99648af590ee8a29c5348"
CITY = "Москва"


def get_weather(city: str, api_key: str) -> dict:
    """Получает данные о погоде через API OpenWeatherMap"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()


def format_weather_message(weather_dict: dict) -> str:
    """Форматирует данные о погоде в читаемое сообщение"""
    temp = weather_dict["main"]["temp"]
    feels_like = weather_dict["main"]["feels_like"]
    description = weather_dict["weather"][0]["description"]
    humidity = weather_dict["main"]["humidity"]
    wind_speed = weather_dict["wind"]["speed"]

    message = (
        f"Температура: {temp}°C\n"
        f"Ощущается как: {feels_like}°C\n"
        f"Описание: {description}\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed} м/с"
    )
    return message


def notify_weather(message: str) -> None:
    """Отправляет уведомление с информацией о погоде"""
    notification.notify(
        title=f"Погода в городе {CITY}",
        message=message,
        app_name="Weather App",
        app_icon=None,
        timeout=10,
    )


def main():
    """Основная логика приложения"""
    try:
        # Получаем данные о погоде
        weather_data = get_weather(CITY, API_KEY)

        # Форматируем сообщение
        weather_message = format_weather_message(weather_data)

        # Отправляем уведомление
        notify_weather(weather_message)

    except requests.RequestException as e:
        notify_weather(f"Ошибка при получении данных: {str(e)}")
    except KeyError as e:
        notify_weather(f"Ошибка в формате данных: {str(e)}")
    except Exception as e:
        notify_weather(f"Неизвестная ошибка: {str(e)}")


if __name__ == "__main__":
    main()
