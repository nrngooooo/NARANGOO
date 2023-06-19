from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/branch')
def branch():
    con = sql.connect("is.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('''
    Select * from branch
    ''')
    b = cur.fetchall()
    return render_template("branch.html",branches = b)

@app.route('/worker')
def worker():
    con = sql.connect("is.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('''
    Select wid, wname, worker.bid, bname from worker inner join branch on branch.bid = worker.bid
    ''')
    b = cur.fetchall()
    return render_template("worker.html",workers = b)

if __name__ == '__main__':
    app.run()