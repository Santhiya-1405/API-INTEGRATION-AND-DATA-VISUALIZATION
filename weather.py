import requests
from datetime import datetime
import matplotlib.pyplot as plt

API_Key = "f2e473e0926f0693cf4c5d51b703b2cc"
city_name = input("Enter the City Name: ")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric"
response = requests.get(URL)
data = response.json()

if data["cod"] != 200:
    print(f"Invalid City: {city_name}")
    exit()
  
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
cloudiness = data["clouds"]["all"]
weather_desc = data["weather"][0]["description"]

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print("\n" + "*" * 60)
print(f"Weather Report for {city_name.upper()}  |  {date_time}")
print("*" * 60)
print(f"Temperature       : {temp} °C")
print(f"Weather Condition : {weather_desc.capitalize()}")
print(f"Humidity          : {humidity} %")
print(f"Wind Speed        : {wind_speed} m/s")
print(f"Cloudiness        : {cloudiness} %")


parameters = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Cloudiness (%)"]
values = [temp, humidity, wind_speed, cloudiness]

plt.figure(figsize=(7, 5))
plt.bar(parameters, values)
plt.title(f"Current Weather Conditions - {city_name.title()}")
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


