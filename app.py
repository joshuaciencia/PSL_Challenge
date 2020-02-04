#!/usr/bin/python3
""" module for platform """
from flask import Flask, render_template, request
from converter import convert

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    """ root page for the platform """
    if request.method == 'POST':
        result = 0
        for state in request.form:
            result += convert(request.form.get(state))
        return "Total of victims in Colombia: " + str(result)
    with open("data.txt") as f:
        states = f.readlines()
    # remove leading/trailing characters
    states = [x.strip() for x in states]
    return render_template('index.html', states=states)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
