from sqlalchemy import create_engine, insert
from sqlalchemy.sql import table, column
from flask import Flask, request
from flask import render_template
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

def save_to_mysql_database(text, ip):
    engine = create_engine('mysql+pymysql://lad:1@138.2.88.234:3306/kha_banh_db')
    with engine.connect() as conn:
        t = table('kha_banh', column('text'), column('ip'))

        stmt = (
            insert(t).values(text=text, ip=ip)
        )
        result = conn.execute(stmt)


@app.route('/', methods= ['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        text = request.form["text"]
        guest_ip = request.environ.get('REMOTE_ADDR')
        save_to_mysql_database(text, guest_ip)

        return render_template('index.html', msg=transform(text))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
