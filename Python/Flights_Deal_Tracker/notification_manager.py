import os
import datetime
import smtplib
from twilio.rest import Client

from data_manager import DataManager

# Constants of Twilio sms service, and email-password for smtp
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SMTP_EMAIL = os.getenv("MY_EMAIL")
SMTP_EMAIL_PASSWORD = os.getenv("SMTP_TOKEN")


class NotificationManager:
    def __init__(self):
        """This class is responsible for sending notifications with flight details."""
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        self.email_body = None

    def send_sms(self, flight_info):
        """Sends user an SMS containing flight deal info"""
        print("Sending flight details via SMS...", end=" ")
        self.email_body = flight_info

        message = self.client.messages.create(
            from_=os.getenv("TWILIO_NUMBER"),
            to=os.getenv("MY_NUMBER"),
            body=flight_info
        )
        print("Done!")
        print(f"SMS SID '{message.sid}'", end="\n\n")

    def send_email(self, emails_list):
        """Sends all users an email with cheap flight deal info"""
        for user in emails_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=SMTP_EMAIL, password=SMTP_EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=SMTP_EMAIL,
                    to_addrs=user["email"],
                    msg=f"Subject: {user["firstName"]}, We got some flight deals for you!\n\n"
                        f"Hi {user["firstName"]} {user["lastName"]}, {self.email_body}".encode("utf-8")
                )
