from flask import Flask, render_template, request
from flask_paginate import Pagination
import sqlite3 as sql
import os

app = Flask(__name__)

@app.route('/')
def index(limit=10):
    con = sql.connect("employee.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(data), css_framework='bootstrap4')
    cur.execute(f"SELECT * FROM user LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("index.html",users=paged_data, paginate=paginate)
@app.route('/asc')
def asc(limit=10):
    con = sql.connect("employee.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user ORDER BY name")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT * FROM user ORDER BY name LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("index.html", users = paged_data, paginate = paginate)
@app.route('/desc')
def desc(limit=10):
    con = sql.connect("employee.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user ORDER BY name desc")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT * FROM user ORDER BY name desc LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("index.html", users = paged_data,paginate=paginate)
if __name__=="__main__":
    app.run(debug=True)