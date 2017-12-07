import datetime


class Reminder2:
    time = ""
    message = ""
    id_number = 0

    def __init__(self, time, message):
        try:
            test_time = datetime.datetime.strptime(time, "%H:%M:%S")
            self.time = time
            self.message = message
            self.reminder = {self.time: self.message}
        except ValueError:
            # for testing purposes
            print("Sorry, the time you gave is not a valid time.")

        # Not sure how to test the validity of the text
