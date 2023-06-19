from django.shortcuts import render, redirect
import sqlite3 as sql

# Create your views here.

def index(request):
    context = {'print': 'Энэ бол нүүр хуудас'}

    return render(request, 'index.html', context)

def department(request):
    if request.method == "GET":
        con = sql.connect("db.sqlite3")
        con.row_factory=sql.Row
        cur = con.cursor()
        cur.execute("SELECT id, depname FROM tbl_department")
        b_data = cur.fetchall()
        return render(request, "department/department.html", context = {'departments': b_data})
    elif request.method == "POST":
        b = request.POST.get('txtDepname')
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute(f"INSERT INTO tbl_department VALUES (NULL, '{b}')")
        con.commit()
        return redirect('/tenhim')

def department_delete(request, id):
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute(f"DELETE FROM tbl_department WHERE id = {id}")
    con.commit()
    return redirect('/tenhim')

def department_edit(request, id):
    if request.method == "GET":
        con = sql.connect("db.sqlite3")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT depname FROM tbl_department WHERE id = {id}")
        b = cur.fetchall()
        b = b[0]['depname']
        return render(request, "department/department_edit.html", context = {'depname': b})
    else:
        bname = request.POST.get('txtDepname')
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute(f"UPDATE tbl_department SET depname='{bname}' WHERE id={id}")
        con.commit()
        return redirect('/tenhim')
