from application import app
from flask import render_template, request, session, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
kUsername = 'esp'
kPassword = 'esp'


# 主页
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='esp@1.0.0')


# 验证身份
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != kUsername or request.form['password'] != kPassword:
            flash('wrong username or password')
            return redirect(url_for('login'))
        flash('login successfully')
        session['username'] = request.form['username']
        return redirect(url_for('upload'))
    return '''
               <form method="post">
               username: <input type="text" name="username"></br>
               password: <input type="password" name="password"></br>
               <input type="submit" value="Login">
               </form>
           '''


# 上传文件的视图
@app.route('/upload')
def upload():
    if 'username' not in session or session['username'] != kUsername:
        return redirect(url_for('login'))
    return render_template('upload.html')


# 上传文件的实际操作
@app.route('/uploading', methods=['POST'])
def uploading():
    f = request.files['file']
    filename = secure_filename(f.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(filepath):
        open(filepath, 'w')
    f.save(filepath)
    return 'file uploaded'


@app.route('/<name>')
def show(name):
    filename = os.path.join(app.config['UPLOAD_FOLDER'], name)
    if not os.path.isfile(filename):
        return '404 not found', 404
    try:
        fp = open(filename, 'r')
        return fp.read()
    except IOError:
        return 'can\'t open file', 404
