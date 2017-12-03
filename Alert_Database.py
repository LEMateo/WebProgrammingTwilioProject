import redis
import threading


class Alert_Database:

    def __init__(self, reminders):
        self.r = redis.Redis()
        self.lock = threading.RLock()

    def get_reminders(self):
        return self.r.keys()

    def new_reminder(self,time,text):
        #create unique identifying number for num
        num=0
        #would the value be the dict with the info? bc the num is the key right?
        #I didnt finish this line
        reminder r=new
        #reminder is the object. Take the time and text and put it into one object, then pull the values when needed
        self.r.append(num,reminder)
    def delete_reminder(self,numID):
        #use for drop
        #numID is the number idenitifier
        #remember to add a name into delete cause I didn't do it yet bc I'm tired rn and don't wanna
        self.r.delete()
