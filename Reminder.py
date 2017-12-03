import datetime


class Reminder(object):
    time = ""
    message = ""
    id_number = 0

    def __init__(self, time, message, id_number):
        # Test time for proper datetime format
        try:
            self.time = datetime.datetime.strptime(time, "%H:%M:%S")
        except ValueError:
            # for testing purposes
            print("Sorry, the time you gave is not a valid time.")

        # Not sure how to test the validity of the text
        self.message = message
        self.id_number = id_number
