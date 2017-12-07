import datetime
from Mock_Database import Mock_Database
from flask import Flask
import ast


app = Flask(__name__)
ad = Mock_Database({})


@app.route('/get')
def get():
    base_results = ad.get_reminders()
    results = []

    for entry in base_results:
        # Converts the each into a string
        test_object = entry.decode("utf-8")
        test_object = ast.literal_eval(test_object)
        print(test_object)
        results.append(test_object)


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


if __name__ == "__main__":
    app.run(debug=True)

