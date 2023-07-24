import smtplib
import os
from dotenv import load_dotenv
import datetime as dt

# https://docs.python.org/3/library/smtplib.html

# load variables from .env files into the environment
load_dotenv()

email_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")
to_email = os.environ.get("TO_EMAIL")


# This is one way to do it

# # set up smtplib connection
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# # https://en.wikipedia.org/wiki/Transport_Layer_Security
# # this is necessary to make our connection secure
# connection.starttls()
#
# # login to my email
# connection.login(user=email_address, password=password)
#
# # actually send the email
# connection.sendmail(from_addr=email_address, to_addrs=to_email, msg="Subject:Hello\n\nThis is the body of my email.")
#
# # close the connection
# connection.close()

# this is another way but it will auto close the connection after the email is sent
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email_address, password=password)
    connection.sendmail(
        from_addr=email_address,
        to_addrs=to_email,
        msg="Subject:Hello\n\nThis is the body of my email."
    )

# # example of datetime module
# now = dt.datetime.now()
#
# # you can tap into the various attribute of now to grab the year/month/day etc
# print(now.year)
#
# # creating a new datetime object
# date_of_brith = dt.datetime(year=1996, month=4, day=1)