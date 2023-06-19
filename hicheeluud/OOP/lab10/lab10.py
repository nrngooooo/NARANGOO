from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

web = Flask(__name__)

@web.route('/')
def index():
    return render_template("index.html")

@web.route('/branch', methods =['GET', 'POST'])
def branch():
    if request.method == "GET":
        # salbariin medeellig db s tataj haruulna
        # get tohioldold branch.html g renderlene
        con = sql.connect("Employee.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_branch")
        b = cur.fetchall()
        return render_template("branch/branch.html", branches = b)
    elif request.method == "POST":
        # tuhain ogogdliig ogodliin sand hadgalna
        # haashaa usreg we gdg g todorhoilno
        bname = request.form['bname']
        con = sql.connect("Employee.db")
        cur = con.cursor()
        if bname is not None:
                cur.execute(f"INSERT INTO tbl_branch VALUES (NULL, '{bname}')")
                con.commit()
        return redirect(url_for('branch'))


@web.route('/worker/create', methods=['GET', 'POST'])
def worker_add():
    if request.method == "GET":
        con = sql.connect("Employee.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_branch")
        b = cur.fetchall()
        cur.execute("SELECT wid, wname, tbl_worker.bid, bname FROM tbl_worker inner join tbl_branch on tbl_branch.bid = tbl_worker.bid")
        w = cur.fetchall()
        return render_template("worker/worker_add.html", branches = b, workers = w)
    elif request.method =="POST":
        bid = request.form["bid"]
        wname = request.form['wname']
        c = sql.connect("Employee.db")
        cur = c.cursor()
        if wname is not None:
            cur.execute(f"INSERT INTO tbl_worker VALUES (NULL, '{wname}',{bid})")
            c.commit()
        return redirect(url_for('worker_add'))

if __name__ == '__main__':
    web.run(debug=True)