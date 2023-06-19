from django.shortcuts import render
from workerApp.models import Worker
import sqlite3 as sql
# Create your views here.
def index(request):
    return render(request, "index.html")

def worker(request):
    con = sql.connect("db.sqlite3")
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute("Select tbl_worker.id, wname, bname from tbl_branch inner join tbl_worker on tbl_worker.bid_id=tbl_branch.id")
    a = cur.fetchall()
    worker_dictionary = {'workers': a}
    return render(request, 'worker/worker.html', context=worker_dictionary)