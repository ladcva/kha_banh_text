from flask import Flask, request, url_for
from flask import render_template, redirect
from random import getrandbits

app = Flask(__name__)

def transform(text):
    new_text = ''

    for char in text:
        if getrandbits(1):
            new_text += char.lower()
        else:
            new_text += char.upper()

    return new_text

@app.route('/', methods= ['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        text = request.form["text"]
        return render_template('index.html', msg=transform(text))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
