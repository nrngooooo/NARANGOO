from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
from flask_paginate import Pagination
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER='static/uploads'
app = Flask(__name__)
app.secret_key="secret key"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif', 'PNG'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM als")
    a = cur.fetchall()
    cur.execute("SELECT * FROM alstailbr")
    ab = cur.fetchall()
    cur.execute("SELECT * FROM erhemzo")
    e = cur.fetchall()
    cur.execute("SELECT * FROM erhemtailbar")
    et = cur.fetchall()
    cur.execute("SELECT * FROM tanilts")
    ta = cur.fetchall()
    cur.execute("SELECT * FROM tatailbar")
    tl = cur.fetchall()
    cur.execute("SELECT * FROM too")
    o = cur.fetchall()
    cur.execute("SELECT * FROM zurag")
    z = cur.fetchall()
    return render_template("index.html", alsiinharaa=a,abtailbar=ab,zorilgo=e, etailbr=et,taniltsuulga=ta,undsentailbar=tl,jagsaalt=o,zurag=z)
# nomiin turul - index
@app.route('/turul')
@app.route('/turul/<msg>')
def turul_list(msg=None):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM turul")
    b = cur.fetchall()
    return render_template("turul/turul_list.html", turuluud = b, msg=msg)

# nomiin turul - nemeh
@app.route('/turul/create', methods = ['GET', 'POST'])
def turul_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT id, tcode, tname FROM turul")
        t = cur.fetchall()
        return render_template("turul/turul_add.html",turuluud = t, msg=msg)
    elif request.method == 'POST':
        try:
            tcode = request.form['txtCode']
            tname = request.form['txtTurul']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO turul VALUES (null, '{tcode}','{tname}')")
            con.commit()
            msg = "Номын төрөл амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Номын төрөл хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('turul_list', msg=msg))

# nomiin turul- zasah
@app.route('/turul/edit/<int:id>', methods = ['POST', 'GET'])
def turul_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('library.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT tcode, tname FROM turul WHERE id={id}")
        t = cur.fetchall()
        tcode = t[0]['tcode']
        tname = t[0]['tname']
        return render_template("turul/turul_edit.html", tname=tname,tcode=tcode)
    elif request.method == 'POST':
        try:
            tcode = request.form['txtCode']
            tname = request.form['txtTurul']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE turul SET tcode= '{tcode}', tname = '{tname}' WHERE id = {id}")
            con.commit()
            msg = "Номын төрөл амжилттай заслаа"
        except:
            con.rollback()
            msg = "Номын төрөл засахад алдаа гарлаа"
        finally:
            return redirect(url_for('turul_list', msg=msg))
#nomiin turul - ustgah
@app.route('/turul/delete/<int:id>')
def turul_delete(id, msg=None):
    try:
        con = sql.connect('library.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM turul WHERE id={id}")
        con.commit()
        msg = "Номын төрөл устгалаа"
    except:
        con.rollback()
        msg = "Номын төрөл устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('turul_list', msg = msg))

# -------------DED TURUL -----------------------------------------------
# nomiin ded turul-index
@app.route('/dedturul')
@app.route('/dedturul/<msg>')
def dedturul_list(msg=None):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM dedturul")
    b = cur.fetchall()
    return render_template("dedturul/dedturul_list.html", dedturul = b, msg=msg)

# nomiin ded turul - nemeh
@app.route('/dedturul/create', methods = ['GET', 'POST'])
def dedturul_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT id, dtcode, dtname FROM dedturul")
        t = cur.fetchall()
        return render_template("dedturul/dedturul_add.html",dedturul = t, msg=msg)
    elif request.method == 'POST':
        try:
            dtcode = request.form['txtDcode']
            dtname = request.form['txtDTurul']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO dedturul VALUES (null, '{dtcode}','{dtname}')")
            con.commit()
            msg = "Номын дэд төрөл амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Номын дэд төрөл хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('dedturul_list', msg=msg))

# nomiin ded turul- zasah
@app.route('/dedturul/edit/<int:id>', methods = ['POST', 'GET'])
def dedturul_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('library.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT dtcode, dtname FROM dedturul WHERE id={id}")
        t = cur.fetchall()
        dtcode = t[0]['dtcode']
        dtname = t[0]['dtname']
        return render_template("dedturul/dedturul_edit.html", dtname=dtname,dtcode=dtcode)
    elif request.method == 'POST':
        try:
            dtcode = request.form['txtDcode']
            dtname = request.form['txtDTurul']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE dedturul SET dtcode= '{dtcode}', dtname = '{dtname}' WHERE id = {id}")
            con.commit()
            msg = "Номын дэд төрөл амжилттай заслаа"
        except:
            con.rollback()
            msg = "Номын дэд төрөл засахад алдаа гарлаа"
        finally:
            return redirect(url_for('dedturul_list', msg=msg))
#nomiin ded turul - ustgah
@app.route('/dedturul/delete/<int:id>')
def dedturul_delete(id, msg=None):
    try:
        con = sql.connect('library.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM dedturul WHERE id={id}")
        con.commit()
        msg = "Номын дэд төрөл устгалаа"
    except:
        con.rollback()
        msg = "Номын дэд төрөл устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('dedturul_list', msg = msg))

# mergejil - index--------------------------------------------------------------------------------------
@app.route('/mergejil')
@app.route('/mergejil/<msg>')
def mergejil_list(msg=None):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM mergejil")
    b = cur.fetchall()
    return render_template("mergejil/mergejil_list.html", mergejiluud = b, msg=msg)

# mergejil - nemeh
@app.route('/mergejil/create', methods = ['GET', 'POST'])
def mergejil_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT id, mcode, mname FROM mergejil")
        t = cur.fetchall()
        return render_template("mergejil/mergejil_add.html",mergejiluud = t, msg=msg)
    elif request.method == 'POST':
        try:
            mcode = request.form['txtMcode']
            mname = request.form['txtMergejil']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO mergejil VALUES (null, '{mcode}','{mname}')")
            con.commit()
            msg = "Мэргэжил амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Мэргэжил хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('mergejil_list', msg=msg))

# mergejil- zasah
@app.route('/mergejil/edit/<int:id>', methods = ['POST', 'GET'])
def mergejil_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('library.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT mcode, mname FROM mergejil WHERE id={id}")
        t = cur.fetchall()
        mcode = t[0]['mcode']
        mname = t[0]['mname']
        return render_template("mergejil/mergejil_edit.html", mname=mname,mcode=mcode)
    elif request.method == 'POST':
        try:
            mcode = request.form['txtMcode']
            mname = request.form['txtMergejil']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE mergejil SET mcode= '{mcode}', mname = '{mname}' WHERE id = {id}")
            con.commit()
            msg = "Мэргэжил амжилттай заслаа"
        except:
            con.rollback()
            msg = "Мэргэжил засахад алдаа гарлаа"
        finally:
            return redirect(url_for('mergejil_list', msg=msg))
#mergejil - ustgah
@app.route('/mergejil/delete/<int:id>')
def mergejil_delete(id, msg=None):
    try:
        con = sql.connect('library.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM mergejil WHERE id={id}")
        con.commit()
        msg = "Мэргэжил устгалаа"
    except:
        con.rollback()
        msg = "Мэргэжил устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('mergejil_list', msg = msg))

# student - index----------------------------------------------------------
@app.route('/student')
@app.route('/student/<msg>')
def student_list(msg=None,limit=5):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode")
    b = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(b), css_framework='bootstrap4')
    cur.execute(f"SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode LIMIT {start}, {limit}")
    paged_data = cur.fetchall()    
    return render_template("student/student_list.html", students=paged_data, paginate=paginate, msg=msg)

@app.route('/student/asc')
def asc(limit=5):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stname")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stname LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("student/student_list.html", students = paged_data, paginate = paginate)

@app.route('/student/desc')
def desc(limit=5):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stname")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stname desc LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("student/student_list.html", students = paged_data, paginate = paginate)
@app.route('/student/codeasc')
def codeasc(limit=5):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stcode")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stcode LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("student/student_list.html", students = paged_data, paginate = paginate)

@app.route('/student/codedesc')
def codedesc(limit=5):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stcode desc")
    u = cur.fetchall()
    page = int(request.args.get("page", 1))
    start = (page - 1) * limit
    paginate = Pagination(page=page,per_page=limit,total=len(u), css_framework='bootstrap4')
    cur.execute(f"SELECT student.id, stcode, stlast,stname, regdug, mname, phone,bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode ORDER BY stcode desc LIMIT {start}, {limit}")
    paged_data = cur.fetchall()
    return render_template("student/student_list.html", students = paged_data, paginate = paginate)
# student - nemeh
@app.route('/student/create', methods = ['POST', 'GET'])
def student_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM mergejil")
        m = cur.fetchall()
        cur.execute("SELECT student.id, stcode,stlast, stname, regdug, phone, mname, bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode")
        o = cur.fetchall()
        return render_template("student/student_add.html",students=o, mergejils=m, msg=msg)
    elif request.method == 'POST':
        try:
            code = request.form['code']
            ovog = request.form['ovog']
            name = request.form['ner']
            regdug = request.form['regdug']
            phone = request.form['utas']
            mname = request.form['mergejil']
            bognoo = request.form['burtognoo']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO student (stcode, stlast, stname, regdug, mcode, phone, bognoo)\
            VALUES ('{code}', '{ovog}','{name}', '{regdug}', '{mname}',{phone} , {bognoo})")
            con.commit()
            msg = "Оюутан амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Оюутан хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('student_list', msg=msg))
            
# student - zasah
@app.route('/student/edit/<int:id>', methods = ['POST', 'GET'])
def student_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT student.id, stcode, stlast, stname, regdug, phone, mname, bognoo FROM student INNER JOIN mergejil ON student.mcode = mergejil.mcode WHERE student.id = {id}")
        b = cur.fetchall()
        student_dicionary = {
        'stcode': str(b[0]['stcode']), 
        'stlast': str(b[0]['stlast']),
        'stname': str(b[0]['stname']),
        'regdug': str(b[0]['regdug']),
        'phone': str(b[0]['phone']),
        'mname': str(b[0]['mname']),
        'bognoo': str(b[0]['bognoo'])
        }
        cur.execute("SELECT * FROM mergejil")
        t = cur.fetchall()
        return render_template("student/student_edit.html", student=student_dicionary, studentuud=b,mergejils=t)
    elif request.method == 'POST':
        try:
            code = request.form['code']
            ovog = request.form['ovog']
            name = request.form['ner']
            regdug = request.form['regdug']
            phone = request.form['utas']
            mcode = request.form['mergejil']
            bognoo = request.form['burtognoo']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE student SET stcode='{code}', stlast = '{ovog}',stname = '{name}', regdug = '{regdug}', mcode = '{mcode}', phone={phone}, bognoo='{bognoo}' WHERE id ={id}")
            con.commit()
            msg = "Оюутны мэдээлэл амжилттай заслаа"
        except:
            con.rollback()
            msg = "Оюутны мэдээлэл засахад алдаа гарлаа"
        finally:
            return redirect(url_for('student_list', msg=msg))
# student - ustgah
@app.route('/student/delete/<int:id>', methods=['GET','POST'])
def student_delete(id):
        try:
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"DELETE FROM student WHERE id='{id}'")
            con.commit()
            msg = "Оюутны мэдээлэл устгалаа"
        except:
            con.rollback()
            msg = "Оюутны мэдээлэл устгахад алдаа гарлаа"
        finally:
            return redirect(url_for('student_list', msg = msg))
# librarian - index--------------------------------------------------------------------------------------
@app.route('/librarian')
@app.route('/librarian/<msg>')
def librarian_list(msg=None):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM librarian")
    b = cur.fetchall()
    return render_template("librarian/librarian_list.html", nomiinSanch = b, msg=msg)

# librarian - nemeh
@app.route('/librarian/create', methods = ['GET', 'POST'])
def librarian_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT id, libcode, liblast, libname, phone, address FROM librarian")
        t = cur.fetchall()
        return render_template("librarian/librarian_add.html",nomiinSanch = t, msg=msg)
    elif request.method == 'POST':
        try:
            libcode = request.form['txtLcode']
            liblast = request.form['txtLlast']
            libname = request.form['txtLname']
            phone = request.form['phone']
            hayg = request.form['hayg']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO librarian VALUES (null, '{libcode}','{liblast}','{libname}',{phone},'{hayg}')")
            con.commit()
            msg = "Номын санч амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Номын санч хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('librarian_list', msg=msg))

# librarian- zasah
@app.route('/librarian/edit/<int:id>', methods = ['POST', 'GET'])
def librarian_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('library.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT libcode, liblast, libname,  FROM librarian WHERE id={id}")
        t = cur.fetchall()
        libcode = t[0]['libcode']
        liblast = t[0]['liblast']
        libname = t[0]['libname']
        phone = t[0]['phone']
        address = t[0]['address']
        return render_template("librarian/librarian_edit.html", libname=libname,libcode=libcode, liblast=liblast,phone=phone,address=address)
    elif request.method == 'POST':
        try:
            libcode = request.form['txtLcode']
            liblast = request.form['txtLlast']
            libname = request.form['txtLname']
            phone = request.form['phone']
            hayg = request.form['hayg']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE librarian SET libcode= '{libcode}',liblast = '{liblast}', libname = '{libname}',phone={phone}, address='{hayg}' WHERE id = {id}")
            con.commit()
            msg = "Номын санч амжилттай заслаа"
        except:
            con.rollback()
            msg = "Номын санч засахад алдаа гарлаа"
        finally:
            return redirect(url_for('librarian_list', msg=msg))
#librarian - ustgah
@app.route('/librarian/delete/<int:id>')
def librarian_delete(id, msg=None):
    try:
        con = sql.connect('library.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM librarian WHERE id={id}")
        con.commit()
        msg = "Номын санч устгалаа"
    except:
        con.rollback()
        msg = "Номын санч устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('librarian_list', msg = msg))

# book - index----------------------------------------------------------
@app.route('/book')
@app.route('/book/<msg>')
def book_list(msg=None):
    con = sql.connect("library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT book.id, bookcode, bookname, author, tname, dtname, bindex, page, bookimg FROM book INNER JOIN dedturul ON book.dtcode = dedturul.dtcode INNER JOIN turul ON book.tcode=turul.tcode")
    b = cur.fetchall()
    return render_template("book/book_list.html", books=b, msg=msg)

# book - nemeh
@app.route('/book/create', methods = ['POST', 'GET'])
def book_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM turul")
        m = cur.fetchall()
        cur.execute("SELECT * FROM dedturul")
        n = cur.fetchall()
        cur.execute("SELECT book.id, bookcode, bookname, author, tname, dtname, bindex, page, bookimg FROM book INNER JOIN dedturul ON book.dtcode = dedturul.dtcode INNER JOIN turul ON book.tcode=turul.tcode")
        o = cur.fetchall()
        return render_template("book/book_add.html",books=o, turuls=m, dedturuls=n, msg=msg)
    elif request.method == 'POST':
        try:
            code = request.form['code']
            name = request.form['name']
            author = request.form['author']
            tcode = request.form['tcode']
            dtcode = request.form['dtcode']
            bindex = request.form['bindex']
            page = request.form['page']
            image = request.files['image']
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                zurag = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO book (bookcode, bookname, author, tcode, dtcode, bindex, page,bookimg)\
            VALUES ('{code}', '{name}','{author}', '{tcode}', '{dtcode}','{bindex}' , {page},'{zurag}')")
            con.commit()
            msg = "Ном амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Ном хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('book_list', msg=msg))
            
# book - zasah
@app.route('/book/edit/<int:id>', methods = ['POST', 'GET'])
def book_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect("library.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT book.id, bookcode, bookname, author, tname, dtname, bindex, page FROM book INNER JOIN turul ON book.tcode = turul.tcode INNER JOIN dedturul ON book.dtcode = dedturul.dtcode WHERE book.id = {id}")
        b = cur.fetchall()
        book_dicionary = {
        'bookcode': str(b[0]['bookcode']), 
        'bookname': str(b[0]['bookname']),
        'author': str(b[0]['author']),
        'tname': str(b[0]['tname']),
        'dtname': str(b[0]['dtname']),
        'bindex': str(b[0]['bindex']),
        'page': str(b[0]['page'])
        }
        cur.execute("SELECT * FROM turul")
        t = cur.fetchall()
        cur.execute("SELECT * FROM dedturul")
        dt = cur.fetchall()
        return render_template("book/book_edit.html", book=book_dicionary, books=b,turuls=t, dedturuls=dt)
    elif request.method == 'POST':
        try:
            code = request.form['code']
            name = request.form['name']
            author = request.form['author']
            tcode = request.form['tcode']
            dtcode = request.form['dtcode']
            bindex = request.form['bindex']
            page = request.form['page']
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"UPDATE book SET bookcode='{code}', bookname = '{name}',author = '{author}', tcode = '{tcode}', dtcode = '{dtcode}', bindex='{bindex}', page='{page}' WHERE id ={id}")
            con.commit()
            msg = "Ном амжилттай заслаа"
        except:
            con.rollback()
            msg = "Ном засахад алдаа гарлаа"
        finally:
            return redirect(url_for('book_list', msg=msg))
# book - ustgah
@app.route('/book/delete/<int:id>', methods=['GET','POST'])
def book_delete(id):
        try:
            con = sql.connect('library.db')
            cur = con.cursor()
            cur.execute(f"DELETE FROM book WHERE id={id}")
            con.commit()
            msg = "Ном устгалаа"
        except:
            con.rollback()
            msg = "Ном устгахад алдаа гарлаа"
        finally:
            return redirect(url_for('book_list', msg = msg))
if __name__ == '__main__':
    app.run(debug=True)