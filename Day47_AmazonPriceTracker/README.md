# Amazon Price Tracker

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day47_AmazonPriceTracker/Amazon-price-tracker.gif" width="800px" alt="Amazon Price Tracker demo"/>

## Introduction

This app will take a url, and web scrape the price off Amazon using BeautifulSoup and send you an email about the item if it is below a target price.

## Future Improvements / Potential Features

Amazon page changes so frequently and from item to item that the script might break if the web page change again. 

I want to add a features where we can use an excel sheet or json to keep track of more than 1 item. Perhaps using Selenium to query list of items individually and inputting the lowest price we can find for each item, then sending user an email about any items that is below the target prices.