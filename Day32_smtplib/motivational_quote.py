import smtplib
import os
from datetime import datetime

from dotenv import load_dotenv
import random
import datetime as dt

# ==================
# grabbing .env info
# ==================
load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

# =================
# Quotes list setup
# =================
quotes_list = []

with open(file="quotes.txt", mode="r") as file:
    # file is the whole txt
    # quote is each line in the file
    # access each quote with a for loop
    for quote in file:
        quotes_list.append(quote)

# =============
# Sending email
# =============

now = dt.datetime.now()

if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        quote = random.choice(quotes_list)
        # opening the connection and securing the route
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=f"Subject:Motivational Quote Monday\n\n{quote}"
        )