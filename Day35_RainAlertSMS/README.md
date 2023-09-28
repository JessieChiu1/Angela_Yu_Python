# Rain Alert Notification with Twilio 🌧️☂️📱 

## Introduction

This Python script provides a rain alert notification using the Twilio API. It fetches weather data from the OpenWeatherMap API based on latitude and longitude coordinates and checks if rain is expected within the next few hours. If rain is detected in the forecast, it sends an SMS notification to a specified phone number using Twilio.

## Required Libraries

You'll need to install the following Python libraries using `pip`:

- To install `requests`, use the following command:
   ```bash
   pip install requests
   pip install python-dotenv
   pip install twilio
   ```

## Usage

Before running the script, follow these setup instructions:

### 1. Configure Environment Variables

Create a `.env` file in the same directory as your script and set the following environment variables:

- `LAT`: Latitude coordinate of the location for which you want weather data.
- `LON`: Longitude coordinate of the location.
- `API_KEY`: Your OpenWeatherMap API key.
- `ACCOUNT_SID`: Your Twilio account SID.
- `AUTH_TOKEN`: Your Twilio authentication token.
- `MY_NUMBER`: Your phone number (where you want to receive rain alerts).
- `TWILIO_NUMBER`: Your Twilio phone number.

### 2. Run the Script

Execute the script. It will fetch weather data, check for rain in the forecast, and send an SMS notification to your specified phone number if rain is expected.

## Notes

- This script fetches a short-term weather forecast, typically within the next few hours.
- You can use services like PythonAnywhere to host and schedule the script to run at specific times.

## Challenges

One of the notable challenges faced during the development of this script was related to Twilio's requirement for verifying toll-free numbers. Twilio has strict verification processes in place to ensure the legitimacy of phone numbers used for sending SMS messages and I had a lot of trouble trying to verified my number.

## Potential Features

1. **Multiple Location Support**: Enable users to receive weather alerts for multiple locations by adding support for storing and monitoring multiple sets of latitude and longitude coordinates.

2. **Weather Forecast Frequency**: Implement an option to specify the frequency of weather forecasts, allowing users to choose hourly, daily, or weekly notifications based on their preferences.

3. **Weather Conditions**: Extend the script to provide detailed information about upcoming weather conditions, including temperature, humidity, and wind speed.
