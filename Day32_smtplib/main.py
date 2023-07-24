import smtplib
import os
from dotenv import load_dotenv

# load variables from .env files into the environment
load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")
app_password = os.environ.get("APP_PASSWORD")
to_email = os.environ.get("TO_EMAIL")

# set up smtplib connection
connection = smtplib.SMTP("smtp.gmail.com", port=587)

# https://en.wikipedia.org/wiki/Transport_Layer_Security
# this is necessary to make our connection secure
connection.starttls()
