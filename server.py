
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

app.secret_key = "21"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(session)
    return render_template('results.html')



if __name__ == "__main__":
    app.run(debug = True)