# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates

## Objective
The goal of this project is to develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system retrieves weather data from the OpenWeatherMap API at configurable intervals and processes the data to generate daily summaries and alerts based on user-defined thresholds.

## Features
- Continuous retrieval of weather data from the OpenWeatherMap API for major Indian cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad.
- Temperature conversion from Kelvin to Celsius or Fahrenheit based on user preference.
- Daily weather summary generation with the following metrics:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- User-configurable alert thresholds for specific weather conditions (e.g., high temperature).
- Visualization of daily summaries, historical trends, and triggered alerts.

## Data Source
This system uses the OpenWeatherMap API as the source of weather data. You must sign up for a free API key to access the data.

Key weather parameters:

- main: Main weather condition (e.g., Rain, Snow, Clear)
- temp: Current temperature in Celsius
- feels_like: Perceived temperature in Celsius
- dt: Time of the data update (Unix timestamp)

## Requirements
- Python 3.x
- Required libraries:
```
pip install requests pandas matplotlib
```
- OpenWeatherMap API key (sign up here).
  
## System Setup
### 1. Clone the repository:
```
git clone https://github.com/yourusername/weather-monitoring-system.git
cd weather-monitoring-system
```
### 2. Install the required dependencies:
```
pip install -r requirements.txt
```
### 3. Set up your API key:

- Add your API key to the config.json file:
```
{
  "api_key": "your_openweathermap_api_key"
}
```
## Functionality
### 1. Data Retrieval
- The system retrieves weather data for six Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) at a configurable interval (e.g., every 5 minutes).
### 2. Data Processing & Rollups
- For each weather update, the system converts temperature values from Kelvin to Celsius or Fahrenheit.
- Daily summaries are generated, including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition (e.g., Rain, Snow, Clear)
### 3. Alerting System
- The user can define custom thresholds for weather conditions (e.g., alert if temperature exceeds 35°C for two consecutive updates).
- Alerts can be displayed in the console or sent via email (additional configuration required for email alerts).
### 4. Visualizations
- The system displays visualizations of daily summaries, historical weather trends, and alerts.

## API Endpoints
- /get_weather_data: Fetches weather data for the specified cities.
- /set_alert_threshold: Allows users to set temperature or weather condition thresholds.
- /get_daily_summary: Provides daily weather summaries and aggregates.
## Usage
### 1. Run the application:
```
python weather_monitoring.py
```
### 2. The system will start retrieving weather data at the specified intervals and storing it in the database for analysis.

### 3. Configure thresholds for temperature or weather conditions:
```
set_alert_threshold(city="Delhi", threshold=35)
```
### 4. View daily summaries:
```
/get_daily_summary
```
## Database Schema
- Weather data is stored in a database for future analysis. Below is an example schema:
sql
```
CREATE TABLE weather_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  city VARCHAR(50),
  temp DECIMAL(5, 2),
  feels_like DECIMAL(5, 2),
  weather_main VARCHAR(50),
  timestamp DATETIME
);

CREATE TABLE daily_summary (
  id INT AUTO_INCREMENT PRIMARY KEY,
  city VARCHAR(50),
  avg_temp DECIMAL(5, 2),
  max_temp DECIMAL(5, 2),
  min_temp DECIMAL(5, 2),
  dominant_condition VARCHAR(50),
  date DATE
);
```
## Test Cases
### 1. System Setup:

- Ensure the system connects to the OpenWeatherMap API successfully using a valid API key.
### 2. Data Retrieval:

-Simulate API calls at configurable intervals and verify the correct parsing of weather data for the specified locations.
### 3. Temperature Conversion:

- Verify that temperature values are correctly converted from Kelvin to Celsius or Fahrenheit based on user preference.
### 4. Daily Weather Summary:

- Simulate a series of weather updates for several days and validate that daily summaries (average, max, min temperatures, dominant weather condition) are computed correctly.
### 5. Alerting System:

- Configure alert thresholds and simulate scenarios where weather data exceeds or violates thresholds. Verify that alerts are triggered appropriately.
## Bonus Features
- Support for additional weather parameters like humidity, wind speed, etc.
- Weather forecast retrieval for predictive insights.
- Extension of visualization functionalities.
## Conclusion
This real-time weather monitoring system is capable of tracking and analyzing weather data across multiple cities, generating daily summaries, and alerting users when conditions exceed specified thresholds. The system is flexible, allowing for the addition of new weather parameters and forecast data.

## License
This project is licensed under the MIT License.

This README covers the purpose of the application, setup instructions, API details, test cases, and bonus features, providing all the information necessary to understand and run the project.






