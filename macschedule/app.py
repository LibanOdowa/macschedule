from flask import Flask, render_template, request

from macschedule import backend

app = Flask(__name__)

test = backend.Backend(open("data.json"))

@app.route("/")
def homepage():
    htmltxt = render_template('homepage.html',the_date = "hello")
    return htmltxt

@app.route('/', methods=['POST'])
def results():
    days = request.values.getlist('days')
    dept = request.values.get('department')
    startTime = request.values.get('startTime')
    endTime = request.values.get('endTime')
    resultshtml = render_template('results.html', results=test.get_results(days, dept, startTime, endTime))
    return resultshtml



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
