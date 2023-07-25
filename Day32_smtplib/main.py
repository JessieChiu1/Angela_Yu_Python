import random
import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import pandas as pd

load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

# ==========
# Data setup
# ==========

df = pd.read_csv("birthday.csv")

data = [{"name": row[0], "email": row[1], "month": row[2], "day": row[3]} for _, row in df.iterrows()]

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# ==========
# Send Email
# ==========

# check today
now = dt.datetime.now()

for person in data:
    if person["month"] == now.month and person["day"] == now.day:
        # setup email template
        letter_template = random.choice(letter_templates)
        with open(f"letter_templates/{letter_template}") as draft:
            draft_content = draft.read()
            letter = draft_content.replace("[NAME]", person["name"]) + "\n"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_address, password=password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
