from django.shortcuts import render, redirect
import sqlite3 as sql 

def index(request):
    return render(request, "index.html")

def worker(request):
    if request.method == "GET":
        con = sql.connect("Employee.db")
        con.rowFactory
        cur = con.cursor()
        cur.execute("Select bid, bname from branch")
        b_data = cur.fetchall()
        cur.execute("SELECT wid, wname, worker.bid, bname FROM worker inner join branch on branch.bid = worker.bid")
        w_data = cur.fetchall()
        dj = {
            'workers': w_data,
            'branches': b_data
        }
        return render(request, "worker/worker.html", context=dj )

def worker_add(request):
    if request.method == "GET":
        con = sql.connect("Employee.db")
        con.row_factory=sql.Row
        cur = con.cursor()
        cur.execute("Select bid, bname from branch")
        b_data = cur.fetchall()
        cur.execute("SELECT wid, wname, worker.bid, bname FROM worker inner join branch on branch.bid = worker.bid")
        w_data = cur.fetchall()
        dcs = {
            'workers': w_data,
            'branches': b_data
        }
        return render(request, "worker/worker_add.html", context=dcs )
    elif request.method =="POST":
        txt_branch = request.POST.get("txt_branch")
        wname = request.POST['wname']
        c = sql.connect("Employee.db")
        cur = c.cursor()
        cur.execute(f"INSERT INTO worker VALUES (NULL, '{wname}',{txt_branch})")
        c.commit()
        return redirect('ajiltan')
def delete_worker(request, id):
    con = sql.connect("Employee.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM worker WHERE wid = {id}")
    con.commit()
    return redirect('ajiltan')
def edit_worker(request, id):
    if request.method == "GET":
        con = sql.connect("Employee.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("Select bid, bname from branch")
        b_data = cur.fetchall()
        cur.execute(f"SELECT wname, bname FROM branch WHERE bid = {id}")
        b = cur.fetchall()
        b = b[0]['bname']
        w = w[0]['wname'] 
        return render(request, "worker/worker_Edit.html", {'bname': b}, {'wname': w})
    else:
        txt_branch = request.POST['txt_branch']
        txt_worker = request.POST['txt_worker']
        con = sql.connect("Employee.db")
        cur = con.cursor()
        cur.execute(f"UPDATE worker SET wname='{txt_worker}', bname='{txt_branch}' WHERE wid={id}")
        con.commit()
        return redirect('ajiltan')
