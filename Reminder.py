import datetime


class Reminder(object):
    time = ""
    message = ""
    id_number = 0

    def __init__(self, time, message, id_number):
        # Test time for proper datetime format
        try:
            self.time = datetime.time.strftime(time, '%H:%M:%S')
        except:


        self.message = message
        self.id_number = id_number
