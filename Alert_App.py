from flask import Flask
app = Flask(__name__)
from Alert_Database import Alert_Database
ad=Alert_Database({})

@app.route('/get')
def get():
    #error check
    results=[]
    #dont know if it works!!
    results=ad.get_reminders()
    #add first 10 reminders in database to results


    return results

#@app.route('/set')
#def set(time, text):
    #error check/formatting check

    #add reminder

    #nothing to return


@app.route('/drop')
def drop(numID):
    #identify the reminder by the number id it was given aka numID
    ad.delete_reminder(numID)

