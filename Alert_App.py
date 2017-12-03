import datetime
from Alert_Database import Alert_Database
from flask import Flask


app = Flask(__name__)
ad = Alert_Database({})


@app.route('/get')
def get():
    # dont know if it works!!
    results = ad.get_reminders()

    # add first 10 reminders in database to results

    # Return the first 10 reminders
    return results


@app.route('/set')
def set(time, text):
    # error check/formatting check
    try:
        test_time = datetime.datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        # for testing purposes
        print("Sorry, the time you gave is not a valid time.")
    # Not sure how to test the text for validity.

    # add reminder - have yet to test
    ad.new_reminder(time, text)

    # nothing to return


@app.route('/drop')
def drop(numID):
    # identify the reminder by the number id it was given aka numID
    # did not test yet!!
    if isinstance(numID, int):
        ad.delete_reminder(numID)
    else:
        print("I'm sorry.", numID,  " is not a valid reminder code.")

