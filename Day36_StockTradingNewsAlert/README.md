# Bitcoin Daily Price Change and News Email Notifier 📈

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day36_StockTradingNewsAlert/Bitcoin-email-alert.gif" width="800px" alt="Bitcoin Daily Price Change and News Email Notifier demo"/>

## Introduction

This app performs the following tasks:

- Fetches Bitcoin data via the Alphavantage API and calculates today's price change.
- Retrieves the top 3 breaking news articles about Bitcoin via NewsAPI.org.
- If the current time is after 6 PM, it sends an email notification about Bitcoin to the user.

This program was designed to be hosted on a site where it runs updates automatically at a certain time of the day. That's why 6 PM was chosen, as the crypto market is open 24/7, 365 days a year.

## Required Libraries

You'll need to install the following Python libraries using `pip`:

- To install `requests`, use the following command:
   ```bash
   pip install requests
   pip install python-dotenv
    ```

## Usage

1. Make sure to set the following environment variables in a `.env` file:

   - `BTC_API_KEY`: Your Alphavantage API key for Bitcoin data.
   - `NEWS_API_KEY`: Your NewsAPI.org API key for fetching news articles.
   - `EMAIL_ADDRESS`: Your email address for sending notifications.
   - `PASSWORD`: Your Gmail app-specific password or two-factor authentication (2FA) code, if applicable.

   To generate a Gmail app-specific password, please follow these steps:

   - Go to [https://myaccount.google.com/](https://myaccount.google.com/).
   - Select "Security" on the left and scroll down to "How you sign in to Google."
   - Enable "2-Step Verification."
   - Click on "2-Step Verification" again and scroll to the bottom.
   - There you can add an App password.
   - Select "Other" from the dropdown list and enter an app name, e.g., "Python Mail," then click "Generate."
   - Copy the generated password - This is the only time you will ever see the password. It is 16 characters with no spaces.
   - Use this App password in your Python code instead of your normal password.

2. Run the script. If the current time is after 6 PM, it will fetch Bitcoin data, calculate the price change, fetch news articles, and send an email notification.

## Future Improvements / Potential Features

To improve the user experience, consider implementing the following features:

- Check if the news articles from NewsAPI are still valid before sending an email, avoiding 404 errors.
- Explore additional Alphavantage APIs to expand the app's capabilities beyond the crypto market.

