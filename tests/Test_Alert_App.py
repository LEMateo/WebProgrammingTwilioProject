import unittest
from unittest import TestCase
# import redis
import fakeredis

from Alert_Database import Alert_Database

# format for data entry is  "HH:MM:SS", "........."
def make_database():
    r = fakeredis.FakeStrictRedis()
    r.flushall()
    r.set('00:00:00', "Hello")
    r.set('01:00:00', "Testing")
    return Alert_Database(r)

def make_empty_database():
    r = fakeredis.FakeStrictRedis()
    r.flushall()
    return Alert_Database({})


class TestProductInventory(TestCase):

    def test_new_empty_inventory(self):
        db = make_empty_database()
        self.assertEqual(0, len(db.get_reminders()))

    #def test_new_nonempty_inventory(self):
    #    db = make_database()
    #    self.assert({'foo': 15, 'bar': 20}, db)





