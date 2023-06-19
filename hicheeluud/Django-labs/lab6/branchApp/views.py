from django.shortcuts import redirect, render
import sqlite3 as sql 

def index(request):
    return render(request, "index.html")

def branch(request):
    if request.method == "GET":
        con = sql.connect("Employee.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM branch")
        b_data = cur.fetchall()
        return render(request, "branch/branch.html", context = {'branches': b_data})
    elif request.method == "POST":
        b = request.POST['txt_branch']
        con = sql.connect("Employee.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO branch VALUES (NULL, '{b}')")
        con.commit()
        return redirect('salbar')

def delete_branch(request, id):
    con = sql.connect("Employee.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM branch WHERE bid = {id}")
    con.commit()
    return redirect('salbar')

def edit_branch(request, id):
    if request.method == "GET":
        con = sql.connect("Employee.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT bname FROM branch WHERE bid = {id}")
        b = cur.fetchall()
        b = b[0]['bname']
        return render(request, "branch/branch_Edit.html", context = {'bname': b})
    else:
        bname = request.POST['txt_branch']
        con = sql.connect("Employee.db")
        cur = con.cursor()
        cur.execute(f"UPDATE branch SET bname='{bname}' WHERE bid={id}")
        con.commit()
        return redirect('salbar')
