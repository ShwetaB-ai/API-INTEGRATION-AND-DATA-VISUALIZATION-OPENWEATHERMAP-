import requests
import matplotlib.pyplot as plt

# 🔑 Replace with your API key
API_KEY = "bb17ef010356ef9d6e862c540a437b32"

# City list
cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]

temperatures = []
humidities = []

# Fetch data from API
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        temperatures.append(temp)
        humidities.append(humidity)
        
        print(f"{city}: Temp={temp}°C, Humidity={humidity}%")
    else:
        print(f"Error fetching data for {city}")

# 📊 Visualization

# Temperature Graph
plt.figure()
plt.bar(cities, temperatures)
plt.title("Temperature in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.show()

# Humidity Graph
plt.figure()
plt.plot(cities, humidities, marker='o')
plt.title("Humidity in Cities")
plt.xlabel("Cities")
plt.ylabel("Humidity (%)")
plt.show()