import datetime
from Alert_Database import Alert_Database
from flask import Flask
import ast
import requests

ad = Alert_Database({})
app = Flask(__name__)


# Returns 10 reminders in database which come up next.
@app.route('/')
def __init__():
    return ad.scan_reminders()


@app.route('/get')
def get():
    return str(ad.get_reminders())


@app.route('/set/<string:time>/<string:text>')
def set(time, text):
    # error check/formatting check
    try:
        test_time = datetime.datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        # for testing purposes
        print("Sorry, the time you gave is not a valid time.")
    # Not sure how to test the text for validity.

    # add reminder - have yet to test
    return ad.new_reminder(time, text)

    # nothing to return


@app.route('/drop/<int:numID>')
def drop(numID):
    # identify the reminder by the number id it was given aka numID
    # did not test yet!!
    if isinstance(numID, int):
        return ad.delete_reminder(numID)
    else:
        response = "I'm sorry. ", numID,  " is not a valid reminder code."
        return response


if __name__ == "__main__":
    app.run(debug=True)

