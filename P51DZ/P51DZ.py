from flask import Flask, render_template, url_for, request,flash,session,redirect, abort,g
import os
import sqlite3
from FDateBase import FDateBase

DATABASE="/tmp/P51DZ.db"
DEBUG = True
SCRET_KEY = '12345678910'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path,'P51DZ.db'))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g,'link_db'):
        g.link_db = connect_db()
    return g.link_db

# app=Flask(__name__)
menu = [{"name":"Кому нужен водонагреватель", "url":"index"},
        {"name":"Накопительный или проточный", "url":"cumulative"},
        {"name":"Кому не нужен ", "url":"not_needed"},
        {"name":"Cколько стоит", "url":"price"},
        {"name":"Обратная связь", "url":"contact"}]


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("index.html",title="Главная", menu=dbase.get_menu())

@app.route("/cumulative")
def cumulative():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('about'))
    return render_template("cumulative.html", title="Накопительный или проточный", menu=dbase.get_menu())



@app.route("/not_needed")
def not_needed():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('about'))
    return render_template("not_needed.html", title="Кому не нужен Водонагреватель", menu=dbase.get_menu())

@app.route("/price")
def price():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("price.html", title="Цена", menu=dbase.get_menu())


@app.route("/contact", methods=["POST","GET"])
def contact():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("contact.html", title="обратная связь", menu=dbase.get_menu())



@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)