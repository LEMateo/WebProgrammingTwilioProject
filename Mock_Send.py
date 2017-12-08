import datetime
from Mock_Database import Mock_Database
import fakeredis
import threading
import ast


class Mock_Methods:
    # runs constantly to scan for expired reminders
    # expired reminders then sent to send_reminder()
    def scan_reminders(self, reminders):
        expired = []
        for rem in reminders:
            r_info = reminders(rem).decode("utf-8")
            r_time = ast.literal_eval(r_info).keys()
            test_time = datetime.datetime.strptime(r_time[0], "%H:%M:%S")
            pass_time = datetime.datetime.strptime("00:01:00", "%H:%M:%S")
            time_diff = datetime.datetime.now() - test_time
            if time_diff < pass_time:
                expired.append(rem)
        if len(expired) != 0:
            for exp_reminder in expired:
                Mock_Methods.send_reminder(exp_reminder)

    def send_reminder(self, reminder):
        print(reminder)


