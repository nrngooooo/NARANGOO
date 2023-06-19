from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/branch', methods=['GET','POST'])
def branch_Insert():
    if request.method=='GET':
        con=sql.connect('Employee.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute('Select * from branch')
        data=cur.fetchall()
        return render_template('branch.html', salbaruud=data)
    elif request.method=='POST':
        salbarNer=request.form['bname']
        con=sql.connect('Employee.db')
        cur=con.cursor()
        cur.execute(f"INSERT INTO branch VALUES(null, '{salbarNer}')")
        con.commit()
        return redirect(url_for('branch_Insert'))
@app.route('/edit/<int:id>',methods=['GET','POST'])
def branch_Edit(id):
    if request.method=='GET':
        con=sql.connect('Employee.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute(f"Select bname from branch WHERE bid={id}")
        data=cur.fetchall()
        sname=data[0]['bname']
        return render_template('branchEdit.html',bname=sname)
    if request.method=="POST":
        sname=request.form['sname']
        con=sql.connect('Employee.db')
        cur=con.cursor()
        cur.execute(f'UPDATE branch SET bname="{sname}" WHERE bid ={id}')
        con.commit()
        return redirect(url_for('branch_Insert'))

@app.route('/delete/<int:id>',methods=['GET','POST'])
def branch_Delete(id):
    con=sql.connect('Employee.db')
    cur=con.cursor()
    cur.execute(f'DELETE FROM branch WHERE bid ={id}')
    con.commit()
    return redirect(url_for('branch_Insert'))
    

if __name__ == "__main__":
    app.run(debug=True)
