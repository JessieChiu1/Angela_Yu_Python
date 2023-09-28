# Amazon Price Tracker 📦🎯

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day47_AmazonPriceTracker/Amazon-price-tracker.gif" width="800px" alt="Amazon Price Tracker demo"/>

## Introduction

This app takes a URL, web scrapes the price off Amazon using BeautifulSoup, and sends you an email if the item's price falls below a specified target.

### Required Libraries

Before running the script, make sure to install the following Python libraries using `pip`:

- To install `requests`, use the following command:
   ```bash
   pip install requests
   pip install bs4
   pip install python-dotenv
   ```

## Setting Up `.env` Variables

1. Create a `.env` file in the same directory as the script.

2. In the `.env` file, add your email address as follows:
EMAIL_ADDRESS=your_email@gmail.com

3. Generate a Gmail App Password:

- Go to [https://myaccount.google.com/](https://myaccount.google.com/).

- Select "Security" on the left and scroll down to "How you sign in to Google."

- Enable "2-Step Verification."

- Click on "2-Step Verification" again and scroll to the bottom.

- There you can add an App password.

- Select "Other" from the dropdown list and enter an app name, e.g., "Amazon Price Tracker," then click "Generate."

- COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.

4. In the `.env` file, add the generated Gmail App Password as follows:
PASSWORD=your_app_password


## Challenge

Testing this script with multiple items revealed a significant challenge. The Amazon HTML layout can change drastically between various item types, such as prime eligible and non-prime eligible items, or between items with different quantities.

Initially, I ensured that the code functioned correctly when distinguishing between prime eligible and non-prime eligible items. However, upon revisiting the code later, I discovered that the layout had changed once again. 

Addressing this challenge requires a thorough reconsideration of the web scraping approach to ensure robustness across various Amazon page layouts. Finding a more adaptable solution for price extraction will be essential.


## Future Improvements / Potential Features

While the current version of the app works well, Amazon's webpage structure frequently changes, making the script susceptible to breaking. To enhance its robustness and add more functionality, consider the following potential features:

1. **Multi-Item Price Tracking**: Implement the ability to track multiple items by using an Excel sheet or JSON file to keep a record of each item's details, including its URL and target price. The script could use Selenium to query each item individually, determine the lowest price found, and then send you an email alert for any items that drop below their respective target prices.

2. **Adaptive Price Scraping**: Address the challenge posed by Amazon's changing HTML layouts. Develop a more adaptive approach to price scraping that can handle variations in page structure, ensuring that the script remains effective even as Amazon updates its website layout. This would involve continuous monitoring and adjustment of the web scraping methodology to accommodate layout changes.

These potential features aim to make the app more versatile and resilient to changes in the Amazon webpage layout, ultimately providing a more reliable and comprehensive price tracking solution.




