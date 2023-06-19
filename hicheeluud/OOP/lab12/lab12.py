from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")
# Tenhim - index
@app.route('/tenhim/', methods = ['POST', 'GET'])
@app.route('/tenhim/<msg>')
def tenhim_list(msg=None):
    if request.method == 'GET':
        con = sql.connect("MU.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM tenhim")
        t = cur.fetchall()
        return render_template("tenhim/tenhim_list.html",tenhims = t, msg=msg)
    elif request.method == 'POST':
        try:
            tname = request.form['txtTenhim']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO tenhim VALUES (null, '{tname}')")
            con.commit()
            msg = "Тэнхим амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Тэнхим хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('tenhim_list', msg=msg))

@app.route('/tenhim/create', methods = ['POST', 'GET'])
def tenhim_add(msg=None):
    if request.method == 'POST':
        try:
            tname = request.form['txtTenhim']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO tenhim VALUES (null, '{tname}')")
            con.commit()
            msg = "Тэнхим амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Тэнхим хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('tenhim_list', msg=msg))
# Tenhim - zasah
@app.route('/tenhim/edit/<int:id>', methods = ['POST', 'GET'])
def tenhim_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('MU.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT tname FROM tenhim WHERE tcode={id}")
        t = cur.fetchall()
        tname = t[0]['tname']
        return render_template("tenhim/tenhim_edit.html", tname=tname)
    elif request.method == 'POST':
        try:
            tname = request.form['txtTenhim']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"UPDATE tenhim SET tname = '{tname}' WHERE tcode = {id}")
            con.commit()
            msg = "Тэнхим амжилттай заслаа"
        except:
            con.rollback()
            msg = "Тэнхим засахад алдаа гарлаа"
        finally:
            return redirect(url_for('tenhim_list', msg=msg))
# tenhim - ustgah
@app.route('/tenhim/delete/<int:id>')
def tenhim_delete(id, msg=None):
    try:
        con = sql.connect('MU.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM tenhim WHERE tcode={id}")
        con.commit()
        msg = "Тэнхим устгалаа"
    except:
        con.rollback()
        msg = "Тэнхим устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('tenhim_list', msg = msg))

# bagsh - index
@app.route('/bagsh')
@app.route('/bagsh/<msg>')
def bagsh_list(msg=None):
    con = sql.connect("MU.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT id, bcode, bovog, bner, gender, aognoo,atname,ename, tname FROM bagsh INNER JOIN tenhim ON bagsh.tcode = tenhim.tcode INNER JOIN alban on bagsh.atcode=alban.atcode INNER JOIN zereg on bagsh.ecode=zereg.ecode")
    b = cur.fetchall()
    return render_template("bagsh/bagsh_list.html", bagshNar = b, msg=msg)

# bagsh - nemeh
@app.route('/bagsh/create', methods = ['POST', 'GET'])
def bagsh_add(msg=None):
    if request.method == 'GET':
        con = sql.connect("MU.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM tenhim")
        tenhims = cur.fetchall()
        cur.execute("SELECT id, bcode, bovog, bner, gender, aognoo, tname FROM bagsh INNER JOIN tenhim ON bagsh.tcode = tenhim.tcode")
        b = cur.fetchall()
        cur.execute("SELECT * FROM alban")
        albans = cur.fetchall()
        cur.execute("SELECT * FROM zereg")
        zeregs = cur.fetchall()
        return render_template("bagsh/bagsh_add.html",  tenhims=tenhims,bagshNar=b, albans=albans, zeregs=zeregs, msg=msg)
    elif request.method == 'POST':
        try:
            code = request.form['txt_code']
            ovog = request.form['txt_ovog']
            ner = request.form['txt_ner']
            huis = request.form['gender']
            ognoo = request.form['ajild_orson']
            atcode = request.form['alban']
            ecode = request.form['zereg']
            tenhim = request.form['tenhim']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO bagsh (bcode, bovog, bner, gender, aognoo, tcode, atcode, ecode)\
                 VALUES ('{code}', '{ovog}', '{ner}', '{huis}', '{ognoo}', {tenhim}, {atcode}, {ecode})")
            con.commit()
            msg = "Багш амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Багш хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('bagsh_list', msg=msg))
            
# bagsh - zasah
@app.route('/bagsh/edit/<int:id>', methods = ['POST', 'GET'])
def bagsh_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect("MU.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT id, bcode, bovog, bner, gender, aognoo, tname, atname,ename FROM bagsh INNER JOIN tenhim ON bagsh.tcode = tenhim.tcode INNER JOIN alban on bagsh.atcode=alban.atcode INNER JOIN zereg on bagsh.ecode=zereg.ecode WHERE id = {id}")
        b = cur.fetchall()
        bagsh_dicionary = {
        'bcode': str(b[0]['bcode']), 
        'bovog': str(b[0]['bovog']),
        'bner': str(b[0]['bner']),
        'gender': str(b[0]['gender']),
        'aognoo': str(b[0]['aognoo']),
        'tname': str(b[0]['tname']),
        'atname': str(b[0]['atname']),
        'ename': str(b[0]['ename'])
        }
        cur.execute("SELECT * FROM tenhim")
        t = cur.fetchall()
        cur.execute("SELECT * FROM alban")
        a = cur.fetchall()
        cur.execute("SELECT * FROM zereg")
        z = cur.fetchall()
        return render_template("bagsh/bagsh_edit.html", bagsh=bagsh_dicionary, bagshNar=b,tenhims=t, albans=a,zeregs=z)
    elif request.method == 'POST':
        try:
            code = request.form['txt_code']
            ovog = request.form['txt_ovog']
            ner = request.form['txt_ner']
            huis = request.form['gender']
            ognoo = request.form['ajild_orson']
            atcode = request.form['alban']
            ecode = request.form['zereg']
            tenhim = request.form['tenhim']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"UPDATE bagsh SET bcode='{code}', bovog = '{ovog}',bner = '{ner}', gender = '{huis}', aognoo = '{ognoo}', atcode='{atcode}', ecode='{ecode}', tcode = {tenhim} WHERE id ={id}")
            con.commit()
            msg = "Багшийн мэдээлэл амжилттай заслаа"
        except:
            con.rollback()
            msg = "Багшийн мэдээлэл засахад алдаа гарлаа"
        finally:
            return redirect(url_for('bagsh_list', msg=msg))
# bagsh - ustgah
@app.route('/bagsh/delete/<int:id>', methods=['GET','POST'])
def bagsh_delete(id):
        try:
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"DELETE FROM bagsh WHERE id='{id}'")
            con.commit()
            msg = "Багшийн мэдээлэл устгалаа"
        except:
            con.rollback()
            msg = "Багшийн мэдээлэл устгахад алдаа гарлаа"
        finally:
            return redirect(url_for('bagsh_list', msg = msg))

# alban index
@app.route('/alban/', methods = ['POST', 'GET'])
@app.route('/alban/<msg>')
def alban_list(msg=None):
    if request.method == 'GET':
        con = sql.connect("MU.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM alban")
        t = cur.fetchall()
        return render_template("alban/alban_list.html",tenhims = t, msg=msg)
    elif request.method == 'POST':
        try:
            atname = request.form['txtAlban']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO alban VALUES (null, '{atname}')")
            con.commit()
            msg = "Албан тушаал амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Албан тушаал хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('alban_list', msg=msg))

# Alban - zasah
@app.route('/alban/edit/<int:id>', methods = ['POST', 'GET'])
def alban_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('MU.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT atname FROM alban WHERE atcode={id}")
        a = cur.fetchall()
        atname = a[0]['atname']
        return render_template("alban/alban_edit.html", atname=atname)
    elif request.method == 'POST':
        try:
            atname = request.form['txtAlban']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"UPDATE alban SET atname = '{atname}' WHERE atcode = {id}")
            con.commit()
            msg = "Албан тушаал амжилттай заслаа"
        except:
            con.rollback()
            msg = "Албан тушаал засахад алдаа гарлаа"
        finally:
            return redirect(url_for('alban_list', msg=msg))
# alban - ustgah
@app.route('/alban/delete/<int:id>')
def alban_delete(id, msg=None):
    try:
        con = sql.connect('MU.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM alban WHERE atcode={id}")
        con.commit()
        msg = "Албан тушаал устгалаа"
    except:
        con.rollback()
        msg = "Албан тушаал устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('alban_list', msg = msg))

# zereg index
@app.route('/zereg/', methods = ['POST', 'GET'])
@app.route('/zereg/<msg>')
def zereg_list(msg=None):
    if request.method == 'GET':
        con = sql.connect("MU.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM zereg")
        t = cur.fetchall()
        return render_template("zereg/zereg_list.html",tenhims = t, msg=msg)
    elif request.method == 'POST':
        try:
            ename = request.form['txtZereg']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO zereg VALUES (null, '{ename}')")
            con.commit()
            msg = "Эрдмийн зэрэг амжилттай хадгаллаа"
        except:
            con.rollback()
            msg = "Эрдмийн зэрэг хадгалахад алдаа гарлаа"
        finally:
            return redirect(url_for('zereg_list', msg=msg))

# zereg - zasah
@app.route('/zereg/edit/<int:id>', methods = ['POST', 'GET'])
def zereg_edit(id, msg=None):
    if request.method == 'GET':
        con = sql.connect('MU.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"SELECT ename FROM zereg WHERE ecode={id}")
        a = cur.fetchall()
        ename = a[0]['ename']
        return render_template("zereg/zereg_edit.html", ename=ename)
    elif request.method == 'POST':
        try:
            ename = request.form['txtZereg']
            con = sql.connect('MU.db')
            cur = con.cursor()
            cur.execute(f"UPDATE zereg SET ename = '{ename}' WHERE ecode = {id}")
            con.commit()
            msg = "Эрдмийн зэрэг амжилттай заслаа"
        except:
            con.rollback()
            msg = "Эрдмийн зэрэг засахад алдаа гарлаа"
        finally:
            return redirect(url_for('zereg_list', msg=msg))
# zereg - ustgah
@app.route('/zereg/delete/<int:id>')
def zereg_delete(id, msg=None):
    try:
        con = sql.connect('MU.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM zereg WHERE ecode={id}")
        con.commit()
        msg = "Эрдмийн зэрэг устгалаа"
    except:
        con.rollback()
        msg = "Эрдмийн зэрэг устгахад алдаа гарлаа"
    finally:
        return redirect(url_for('zereg_list', msg = msg))

if __name__ == '__main__':
    app.run(debug=True)