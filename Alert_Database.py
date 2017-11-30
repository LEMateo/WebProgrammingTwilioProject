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
        self.r.append(num,)

