import redis
import threading
import Reminder


class Alert_Database:

    def __init__(self, reminders):
        # Create base database for reminders
        self.r = redis.Redis()
        self.lock = threading.RLock()

        # Create initial id_num to act as key for reminders in database
        self.id_num = 0

    def get_reminders(self):
        return self.r.keys()

    def new_reminder(self, time, text):
        # reminder_instance is the object.
        # Take the time and text and put it into one object, then pull the values when needed
        reminder_instance = Reminder.Reminder(time, text, self.id_num)

        self.r.set(self.id_num, reminder_instance)

        # increment ID to prep for next reminder
        self.id_num += 1

    def delete_reminder(self, numID):
        # use for drop
        # numID is the number identifier

        # remember to add a name into delete cause I didn't do it yet bc I'm tired rn and don't wanna
        self.r.delete()
