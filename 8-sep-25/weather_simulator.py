'''4. Weather Simulator (`random`)
 
* Input: None
* Output: `"Weather: Sunny, Temp: 32°C"`'''

import random

def simulate_weather():
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy", "Snowy"]
    weather = random.choice(weather_conditions)
    temp = random.randint(-10, 40)  
    return f"Weather: {weather}, Temp: {temp}°C"

print(simulate_weather())
