# Bitcoin Daily Price Change and News Email Notifier

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day36_StockTradingNewsAlert/Bitcoin-email-alert.gif" width="800px" alt="Bitcoin Daily Price Change and News Email Notifier demo"/>

## Introduction

This app will:
- fetch the Bitcoin data via Alphavantage API and calculate today's price change
- fetch the top 3 breaking news about Bitcoin via NewsAPI.org
- If it is after 6PM, it will send an email about Bitcoin to the user.

This program was intended to be host on a site where it will ran the update automatically at certain time of the day. That's why I chose 6PM specifically, because the crypto market is open 24/7 365.

## Future Improvements / Potential Features

Some of the news article from NewsAPI lead to 404 page, I think it would be really good if we can check if the article is still valid before we send an email.

Alphavantage has a lot of other APIs, I can add more alert and expand it beyond crypto market. 