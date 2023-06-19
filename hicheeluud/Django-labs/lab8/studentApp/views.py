from django.shortcuts import render, redirect
import sqlite3 as sql

def index(request):
    context = {'print': 'Энэ бол нүүр хуудас'}

    return render(request, 'index.html', context)

def student(request):
    con = sql.connect("db.sqlite3")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("Select * from tbl_department")
    drows = cur.fetchall()
    cur.execute("Select tbl_student.id, stlast, stname, depname from tbl_student inner join tbl_department on tbl_student.depcode_id=tbl_department.id")
    rows = cur.fetchall()
    context = {'students': rows,
               'departments': drows
               }
    return render(request, 'student/student.html', context)


def student_add(request):
    if request.method == 'GET':
        con = sql.connect("db.sqlite3")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("Select * from tbl_department")
        drows = cur.fetchall()
        cur.execute("Select tbl_student.id, stlast, stname, depname from tbl_student inner join tbl_department on tbl_student.depcode_id=tbl_department.id")
        rows = cur.fetchall()
        context = {'students': rows,
                   'departments': drows
                   }
        con.close()
        return render(request, "student/student_add.html", context)
    elif request.method == 'POST':
        stlast = request.POST.get('txtStlast')
        stname = request.POST.get('txtStname')
        bid = request.POST.get('depname')
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO tbl_student VALUES(NULL, '{stlast}', '{stname}', {bid})")
        con.commit()
        con.close()
        return redirect('/oyutan')


def student_edit(request, id):
    if request.method == 'GET':
        con = sql.connect("db.sqlite3")
        con.row_factory = sql.Row
        cur = con.cursor()
        context = {}
        cur.execute("SELECT * FROM tbl_department")
        context['departments'] = cur.fetchall()
        cur.execute(
            f"""SELECT stlast, stname, depcode_id FROM tbl_student WHERE id={id}""")
        row = cur.fetchall()
        context['ovog'] = row[0]['stlast']
        context['oyutan'] = row[0]['stname']
        context['depname'] = row[0]['depcode_id']
        con.close()
        return render(request, "student/student_edit.html", context)
    elif request.method == 'POST':
        stlast = request.POST.get('txtStlast')
        stname = request.POST.get('txtStname')
        bid = request.POST.get('depname')
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute(f"UPDATE tbl_student SET stlast='{stlast}', stname='{stname}', depcode_id={bid} WHERE id={id}")
        con.commit()
        con.close()
        return redirect("/oyutan")
    
def student_delete(request, id):
    con = sql.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute(f"DELETE FROM tbl_student WHERE id = {id}")
    con.commit()
    con.close()
    return redirect('/oyutan')