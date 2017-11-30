import redis
import threading


class Alert_Database:

    def __init__(self, reminders):
        self.r = redis.Redis()
        self.lock = threading.RLock()

    def get_reminders(self):
        return self.r.keys()
