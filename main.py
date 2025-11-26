# working with dictionaries
from pyscript import display


weather_today = {
    "location" : "Manila",
    "temperature_celsius" : 32,
    "humidity" : 78,
    "condition" : "Sunny"
}   # specifying dictionaries

display(weather_today, target="output")
display(weather_today["temperature_celsius"], target="output")  # display only temperature

weather_today["condition"] = "Cloudy"  # updating value
weather_today["Heat_Index"] = 38  # adding new key-value pair
display(weather_today, target="output")