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
        reminders = self.r.keys()
        results = reminders[0: 10]

        return results

    def new_reminder(self, time, text):
        # reminder_instance is the object.
        # Take the time and text and put it into one object, then pull the values when needed
        reminder_instance = Reminder.Reminder(time, text, self.id_num)

        # Adds the new reminder to the database.
        self.r.set(self.id_num, reminder_instance)

        # It might be a good idea to sort the reminders by time

        # Increment id_num to prepare for next reminder
        self.id_num += 1

    def delete_reminder(self, numID):
        # use for drop
        # numID is the unique identifying number

        selected_entry = self.r.get(numID)
        # I think it would be good (but not necessary) to implement some code which does the following:
        # request for confirmation of deletion (y/n)


        # remember to add a name into delete cause I didn't do it yet bc I'm tired rn and don't wanna
        self.r.delete(numID)
