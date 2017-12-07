import fakeredis
import threading
import Reminder_2
import ast


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
        self.r.set(self.id_num, reminder_instance.reminder)
        print("Reminder successfully added.  The reminder's ID is ", self.id_num, ".")

        # It might be a good idea to sort the reminders by time
        self.r.sort(self.r, by=time)

        # Increment id_num to prepare for next reminder
        self.id_num += 1

    def delete_reminder(self, numID):
        # use for drop
        # numID is the unique identifying number

        selected_entry = self.r.get(numID)
        print(selected_entry)
        if(selected_entry == None):
            print("I'm sorry.", numID, " is not a valid reminder code.")
        else:
            selected_entry = selected_entry.decode("utf-8")

            # Request for confirmation of deletion.
            response = input("Are you sure you want to delete the reminder, " + selected_entry + " ?")
            if response != "y" and response != "n":
                print("Sorry, that is not a valid response.")
            else:
                if response == "y":
                    self.r.delete(numID)
                    print("Reminder deleted.")
                if response == "n":
                    print("Deletion canceled.")