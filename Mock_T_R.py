import Mock_Database
import requests
import os


class Twilio_Reminder:
    def send_reminder(self, message):
        base = "https://api.twilio.com/2010-04-01/Accounts/"
        accountSid = "AC959860f3555ba1e035d5bfc59ae19a1b"
        authToken = "9ae3868b4defb5f5dbf94144910364ba"

        second_base = base + accountSid + "/Messages"

        params = {'To': "+14846026317", 'From': "+14842323208", 'Body': message}
        auth = (accountSid, authToken)
        result = requests.post(second_base, data=params)

        print("reminder ", message, " sent")
