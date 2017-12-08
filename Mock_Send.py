import datetime
from Mock_Database import Mock_Database
import fakeredis
import threading
import ast



class Mock_Methods:
    # runs constantly to scan for expired reminders
    # expired reminders then sent to send_reminder()
    def __init__(self, outside_rem):
        self.expired = []



