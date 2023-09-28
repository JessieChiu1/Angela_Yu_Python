# Apartment Hunt 🏢🕵️‍♂️

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day53_ApartmentHunt/Apartment-Hunt.gif" width="800px" alt="Apartment Hunt Demo"/>

## Introduction

This project automates the process of searching for minimum one-bedroom apartments priced under $2,200 on [Apartments.com](https://www.apartments.com/). It collects apartment details and fills in a Google Form with this information.

### Project Tasks:

1. Navigate to [Apartments.com](https://www.apartments.com/).
2. Set search parameters to find:
   - Minimum one-bedroom apartments
   - Apartments priced under $2,200
3. Collect apartment details (address, price, and URL) and store them in a list.
   - For apartments with price ranges, separate entries are created for the lower and upper bound prices.
4. Populate a Google Form with apartment information.

You can view the Google Sheets output of the demo video [here](https://docs.google.com/spreadsheets/d/1g0xwusFaeRjwXKe4OZsRIicZP05xDEWxflRUruhu5jE/edit?usp=sharing).

## Required Libraries

To run this script, you'll need to install the following Python libraries using `pip`:

```bash
pip install selenium
```

## Challenges

During development, the following challenges were encountered:

1. **Updating Search Results**: The code identified the apartment list container too quickly, before the actual search results were updated. To overcome this, a workaround was implemented:
   - Set the parameters (less than $2,200 and minimum one-bedroom).
   - Wait for 5 seconds to allow the URL to update based on our parameters.
   - Refresh the page to search for the new search results.

2. **Web Scraping Variations**: Web scraping apartment addresses, prices, and URLs posed challenges due to variations in HTML structure:
   - Address: An `if` statement was used to handle cases where the HTML tag sometimes didn't contain the address, but the element exist.
   - Price: A `try/except` statement was used to address instances where the price element didn't exist, resulting in a `NoSuchElementError` and requiring the script to search for another price element.

## Potential Features

Here's a potential feature for future development:

1. **User-Defined Location**: Allow users to input their desired location instead of hardcoding it as 'Brooklyn, NY'.
2. **Customizable Parameters**: Let users choose their search parameters to find apartments that match their preferences.
3. **Excel Integration**: Create an Excel Macro to perform basic operations (mean, median, mode) on the collected data and generate tables, charts, and graphs for analysis.
