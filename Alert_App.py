from flask import Flask
app = Flask(__name__)

@app.route('/get')
def get():
    #error check
    results=[]

    #add first 10 reminders in database to results


    return results

#@app.route('/set')
#def set():

#@app.route('/drop')
#def drop():