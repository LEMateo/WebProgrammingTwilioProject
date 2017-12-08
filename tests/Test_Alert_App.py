import unittest
from unittest import TestCase
import fakeredis
import datetime
from Mock_Database import Mock_Database
from Mock_Send import Mock_Methods


def make_empty_database():
    r = fakeredis.FakeStrictRedis()
    r.flushall()
    return Mock_Database({})


class TestReminderDatabase(TestCase):

    def test_empty_database(self):
        db = make_empty_database()
        self.assertEqual(0, len(db.get_reminders()))
        db.delete_reminder(4)
        self.assertEqual("I'm sorry. 4 is not a valid reminder code.", db.delete_reminder(4))
        testTime = datetime.datetime.strptime("01:00:00", "%H:%M:%S")
        subTime = datetime.datetime.strptime("0:00:10", "%H:%M:%S")
        print(testTime - subTime)


    def one_reminder(self):
        db = make_empty_database()
        db.new_reminder("00:00:00", "Hello")
        self.assertEqual(1, len(db.get_reminders()))
        db.delete_reminder(0)
        self.assertEqual(0, len(db.get_reminders()))

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
        # Tests for removing almost all but first entry
        db.delete_reminder(1)
        db.delete_reminder(2)
        db.delete_reminder(3)
        db.delete_reminder(4)
        db.delete_reminder(5)
        db.delete_reminder(6)
        db.delete_reminder(7)
        db.delete_reminder(8)
        db.delete_reminder(9)
        self.assertEqual(1, len(db.get_reminders()))
        print(db.get_reminders())
        self.assertEqual([{'0': {'00:00:00': 'R1'}}], db.get_reminders())

    def test_eleven_reminders(self):
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
        db.delete_reminder(0)
        self.assertEqual(10, len(db.get_reminders()))

    def test_add_duplicate_entry(self):
        db = make_empty_database()
        db.new_reminder("1:00:00", "R1")
        db.new_reminder("1:00:00", "R1")
        self.assertEqual(2,len(db.get_reminders()))

    def test_invalid_insertion(self):
        db = make_empty_database()
        response = db.new_reminder("25:00:00", "R1")
        self.assertEqual("Sorry, the time you gave is not a valid time.", response)
        self.assertEqual(0, len(db.get_reminders()))

    def test_remove_one_of_two(self):
        db = make_empty_database()
        db.new_reminder("2:00:00", "R1")
        db.new_reminder("5:00:00", "R2")
        db.delete_reminder(1)
        self.assertEqual(1, len(db.get_reminders()))

    def test_invalid_removals(self):
        db = make_empty_database()
        db.new_reminder("2:00:00", "R1")
        db.new_reminder("5:00:00", "R2")
        db.delete_reminder(3)
        self.assertEqual(2, len(db.get_reminders()))
        db.delete_reminder(0)
        self.assertEqual("I'm sorry. 0 is not a valid reminder code.", db.delete_reminder(0))

    def test_expired_reminders(self):
        db = make_empty_database()
        db.new_reminder("20:50:00", "Expired")
        db.new_reminder("20:49:00", "Expired")
        db.new_reminder("21:45:00", "Not Expired")
        db.new_reminder("00:45:00", "Not Expired")
        Mock_Methods.scan_reminders(db.get_reminders())






    #def test_sorted_reminders(self):
    #    db = make_empty_database()
    #    db.new_reminder("4:00:00", "Number 4")
    #    db.new_reminder("1:00:00", "Number 1")
    #    db.new_reminder("3:00:00", "Number 3")
    #    db.new_reminder("5:00:00", "Number 5")
    #    db.new_reminder("5:55:55", "Number 6")
    #    db.new_reminder("2:00:00", "Number 2")
    #    print(db.get_reminders())
    #    self.assertEqual([{'1': {'01:00:00': 'Number 1'}}, {'5': {'02:00:00': 'Number 2'}}, {'2': {'03:00:00': 'Number 3'}}, {'0': {'04:00:00': 'Number 4'}}, {'3': {'05:00:00': 'Number 5'}}, {'4': {'05:55:55': 'Number 6'}}], db.get_reminders())


