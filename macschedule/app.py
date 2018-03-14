from flask import Flask, render_template, request

from macschedule import cmdInterface

app = Flask(__name__)

test = cmdInterface.Backend(open("macschedule/data.json"))

@app.route("/")
def homepage():
    htmltxt = render_template('homepage.html',the_date = "hello")
    return htmltxt

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.values.getlist('days')
    print(text)
    resultshtml = render_template('results.html', results=test.get_results(text))
    return resultshtml


# def get_results(daylist):
#     data = json.load(open("macschedule/data.json"))
#     days = ''.join(daylist)
#     results = []
#     for i in data:
#         if i["days"] in days:
#             results.append(i)
#     return results

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
