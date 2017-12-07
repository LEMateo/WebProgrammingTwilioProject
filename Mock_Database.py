import fakeredis
import threading
import Reminder_2
import ast
import datetime


class Mock_Database:

    def __init__(self, reminders):
        # Create base database for reminders
        self.r = fakeredis.FakeStrictRedis()
        self.lock = threading.RLock()

        # Create initial id_num to act as key for reminders in database
        self.id_num = 0

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
