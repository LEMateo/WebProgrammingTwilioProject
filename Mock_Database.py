import fakeredis
import threading
import Reminder_2
import ast
import datetime
from datetime import timedelta
import requests
import os


class Mock_Database:

    def __init__(self, reminders):
        # Create base database for reminders
        self.r = fakeredis.FakeStrictRedis()
        self.lock = threading.RLock()

        # Create initial id_num to act as key for reminders in database
        self.id_num = 0
        self.expired = []
        self.sent_message = ""
        #threading.Timer(30, self.send_reminder()).start()

    def get_reminders(self):
        reminders = self.r.keys()
        base_results = reminders[0: 10]
        results = []

        for i in range(0, len(base_results)):
            # Converts the each into a string
            key = base_results[i].decode("utf-8")
            info = self.r.get(base_results[i]).decode("utf-8")
            info = {key: ast.literal_eval(info)}

            results.append(info)

        self.scan_reminders()
        return results

    def new_reminder(self, time, message):
        # reminder_instance is the object.
        # Take the time and text and put it into one object, then pull the values when needed
        reminder_instance = Reminder_2.Reminder2(time, message)

        # Adds the new reminder to the database.
        try:
            test_time = datetime.datetime.strptime(time, "%H:%M:%S")
            self.r.set(self.id_num, reminder_instance.reminder)
            print("Reminder successfully added. The reminder's ID is", self.id_num, ".")

            # It might be a good idea to sort the reminders by time
            # self.r.sort(self.r, by=time)

            # Increment id_num to prepare for next reminder
            self.id_num += 1
        except ValueError:
            # for testing purposes
            print("Sorry, the time you gave is not a valid time.")
            return "Sorry, the time you gave is not a valid time."

    def delete_reminder(self, numID):
        # use for drop
        # numID is the unique identifying number

        selected_entry = self.r.get(numID)
        if selected_entry is None:
            response = "I'm sorry. " + str(numID) + " is not a valid reminder code."
        else:
            selected_entry = selected_entry.decode("utf-8")

            # Request for confirmation of deletion.
            user_input = input("Are you sure you want to delete the reminder, " + selected_entry + " ?")
            if user_input != "y" and user_input != "n":
                response = "Sorry, that is not a valid response."
            else:
                if user_input == "y":
                    self.r.delete(numID)
                    response = "Reminder deleted."
                if user_input == "n":
                    response = "Deletion canceled."
        return response

    def scan_reminders(self):
        self.expired = []
        for rem in self.r.keys():
            r_info = self.r.get(rem).decode("utf-8")
            r_time = list(ast.literal_eval(r_info))
            print(r_time)
            rem_t = datetime.datetime.strptime(r_time[0], "%H:%M:%S")
            rem_time = timedelta(hours=rem_t.hour, minutes=rem_t.minute, seconds=rem_t.second)
            pass_time_one = datetime.datetime.strptime("00:01:00", "%H:%M:%S").time()
            pass_time_two = datetime.datetime.strptime("23:59:00", "%H:%M:%S").time()
            time_diff = (datetime.datetime.now() - rem_time).time()
            if time_diff < pass_time_one or time_diff > pass_time_two:
                self.expired.append(rem)
        if len(self.expired) != 0:
            self.send_reminder()

    def send_reminder(self):
        for re in self.expired:
            info = self.r.get(re).decode("utf-8")
            m_value = ast.literal_eval(info)
            m_key = list(m_value)
            self.sent_message = m_value.get(m_key[0])
            self.push_reminder()

    def push_reminder(self):
        base = "https://api.twilio.com/2010-04-01/Accounts/"
        accountSid = os.environ['TWILIO_SID']
        authToken = os.environ['TWILIO_ACCESS_TOKEN']

        second_base = base + accountSid + "/Messages"

        params = {'To': "+14846026317", 'From': "+14842323208", 'Body': self.sent_message}
        auth = (accountSid, authToken)
        result = requests.post(second_base, auth=auth, data=params)

        print("reminder ", self.sent_message, " sent")



