from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3 as sql
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER='static/uploads'
app=Flask(__name__)
app.secret_key="secret key"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif', 'PNG'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method=='GET':
        con=sql.connect('school.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute('SELECT * FROM student')
        a=cur.fetchall()
        return render_template('index.html', students=a)
    elif request.method=="POST":
        con=sql.connect('school.db')
        cur=con.cursor()
        sname=request.form['sname']
        image=request.files['image']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            zurag = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cur.execute(f'INSERT INTO student VALUES(NULL, "{zurag}", "{sname}")')
        con.commit()
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def o_delete(id):
    try:
        con = sql.connect('school.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM student WHERE id={id}")
        con.commit()
    except:
        con.rollback()
    finally:
        return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)