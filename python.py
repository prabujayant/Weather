import requests
import time
import sqlite3
from datetime import datetime

API_KEY = 'fa93c7fb63df968a6770adf22d2f5209'
METROS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
API_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

def get_weather_data(city, api_key):
    url = API_URL.format(city=city, key=api_key)
    response = requests.get(url)
    return response.json()

# Fetch data for all metros
def fetch_weather_data(api_key):
    weather_data = {}
    for city in METROS:
        data = get_weather_data(city, api_key)
        weather_data[city] = {
            "main": data['weather'][0]['main'],
            "temp": kelvin_to_celsius(data['main']['temp']),
            "feels_like": kelvin_to_celsius(data['main']['feels_like']),
            "timestamp": datetime.fromtimestamp(data['dt'])
        }
    return weather_data

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def kelvin_to_fahrenheit(kelvin_temp):
    return (kelvin_temp - 273.15) * 9/5 + 32

def setup_database():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_summary (
                        city TEXT,
                        date TEXT,
                        avg_temp REAL,
                        max_temp REAL,
                        min_temp REAL,
                        dominant_condition TEXT)''')
    conn.commit()
    return conn

def store_summary(conn, city, date, avg_temp, max_temp, min_temp, dominant_condition):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                      (city, date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()

def calculate_daily_summary(weather_data):
    avg_temp = sum(d['temp'] for d in weather_data) / len(weather_data)
    max_temp = max(d['temp'] for d in weather_data)
    min_temp = min(d['temp'] for d in weather_data)
    dominant_condition = max(set([d['main'] for d in weather_data]), key=[d['main'] for d in weather_data].count)
    return avg_temp, max_temp, min_temp, dominant_condition

def process_daily_summary(conn, city, weather_data):
    date = weather_data[0]['timestamp'].strftime('%Y-%m-%d')
    avg_temp, max_temp, min_temp, dominant_condition = calculate_daily_summary(weather_data)
    store_summary(conn, city, date, avg_temp, max_temp, min_temp, dominant_condition)

def check_thresholds(city, weather_data, temp_threshold, consecutive_threshold):
    consecutive_count = 0
    for i in range(len(weather_data) - 1):
        if weather_data[i]['temp'] > temp_threshold:
            consecutive_count += 1
        else:
            consecutive_count = 0
        
        if consecutive_count >= consecutive_threshold:
            print(f"Alert! Temperature in {city} exceeded {temp_threshold}°C for {consecutive_threshold} consecutive updates.")
            consecutive_count = 0



def main():
    conn = setup_database()
    interval = 300  # Fetch data every 5 minutes
    temp_threshold = 35  # Threshold for triggering alerts
    consecutive_threshold = 2  # Consecutive breaches required for an alert
    
    while True:
        all_weather_data = fetch_weather_data(API_KEY)
        
        for city, data in all_weather_data.items():
            print(f"Weather Data for {city}: {data}")
            
            # Process the weather data and store the summary
            process_daily_summary(conn, city, [data])
            
            # Check for alerts
            check_thresholds(city, [data], temp_threshold, consecutive_threshold)
        
        # Wait for the next interval
        time.sleep(interval)

if __name__ == "__main__":
    main()