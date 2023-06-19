from flask import Flask, request, render_template
f = Flask(__name__)
@f.route('/')
def index():
    return render_template("index.html")
@f.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        file=request.files['zurag']
        fName=file.filename
        file.save(f'uploads/{fName}.jpg')
    return render_template("upload.html")
if __name__== "__main__":
    f.run(debug=True)