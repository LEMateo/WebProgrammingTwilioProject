import unittest
from unittest import TestCase
# import redis
import fakeredis
from Reminder import Reminder

# Converts string to dictionary
import ast

from Mock_Database import Mock_Database

# format for data entry is  "HH:MM:SS", "........."

# I don't think this creation statement works for our database
# def make_database():
#    r = fakeredis.FakeStrictRedis()
#    r.flushall()
#    r.set('00:00:00', "Hello")
#    r.set('01:00:00', "Testing")
#    return Alert_Database(r)


def make_empty_database():
    r = fakeredis.FakeStrictRedis()
    r.flushall()
    return Mock_Database({})


class TestReminderDatabase(TestCase):

    def test_new_empty_database(self):
        db = make_empty_database()
        self.assertEqual(0, len(db.get_reminders()))

    def test_add_one_reminder(self):
        db = make_empty_database()
        db.new_reminder("00:00:00", "Hello")
        self.assertEqual(1, len(db.get_reminders()))
        # self.assertEqual({0: {"00:00:00", "Hello"}}, db)

    def test_add_ten_reminders(self):
        db = make_empty_database()
        db.new_reminder("00:00:00", "R1")
        db.new_reminder("01:00:00", "R2")
        db.new_reminder("02:00:00", "R3")
        db.new_reminder("03:00:00", "R4")
        db.new_reminder("04:00:00", "R5")
        db.new_reminder("05:00:00", "R6")
        db.new_reminder("06:00:00", "R7")
        db.new_reminder("07:00:00", "R8")
        db.new_reminder("08:00:00", "R9")
        db.new_reminder("09:00:00", "R10")
        self.assertEqual(10, len(db.get_reminders()))
        #print(db.r.scan())

    def test_add_eleven_reminders(self):
        db = make_empty_database()
        db.new_reminder("00:00:00", "R1")
        db.new_reminder("01:00:00", "R2")
        db.new_reminder("02:00:00", "R3")
        db.new_reminder("03:00:00", "R4")
        db.new_reminder("04:00:00", "R5")
        db.new_reminder("05:00:00", "R6")
        db.new_reminder("06:00:00", "R7")
        db.new_reminder("07:00:00", "R8")
        db.new_reminder("08:00:00", "R9")
        db.new_reminder("09:00:00", "R10")
        db.new_reminder("10:00:00", "R11")
        self.assertEqual(10, len(db.get_reminders()))
        #for key in db.r.keys():
        #    print(key)
        #print(db.r.get(0))
        # Converts the entry into a string
        #test_object = db.r.get(0).decode("utf-8")
        #test_object = ast.literal_eval(test_object)
        #print(test_object.keys())

    # test ideas to add later

    def test_add_duplicate_entry(self):
        db = make_empty_database()
        db.new_reminder("1:00:00","R1")
        db.new_reminder("1:00:00","R1")
        self.assertEqual(2,len(db.get_reminders()))

    def test_invalid_insertion(self):
        db=make_empty_database()
        try:
            db.new_reminder("25:00:00","R1")
        except:
            print()
        self.assertEqual(0,len(db.get_reminders()))

    # def test_invalid_numID_removal(self):

    # def test_remove_from_empty_database(self):

    # def test_remove_only_entry(self):

    # def test_remove_one_of_ten(self):

    # def rest_remove_one_of_eleven(self):

    # def test_remove_nine_of_ten(self):

    # def test_remove_all(self):

    # def test_duplicate_removal(self):




