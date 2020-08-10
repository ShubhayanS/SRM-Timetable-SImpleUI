import os
from flask import Flask, render_template, request, session, redirect,flash,url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import os
import math
from datetime import datetime
from flask_caching import Cache
from flask_mysqldb import MySQL
from flask import jsonify
from flask import json
import requests
from flask import send_from_directory


UPLOAD_FOLDER='./uploads/'
ALLOWED_EXTENSIONS ={'txt','pdf','jpg','png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.secret_key = 'development key'

app.config['MYSQL_HOST'] = 'dataly.database.windows.net'
app.config['MYSQL_USER'] = 'dataly'
app.config['MYSQL_PASSWORD'] = 'uG5qMZxv'
app.config['MYSQL_DB'] = 'dataly'
mysql = MySQL(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/',methods= ["GET",'POST'])
@app.route('/home',methods= ["GET",'POST'])
@cache.cached(timeout=50)
def home():
    return render_template('form.html')


@app.route('/resume',methods= ["GET",'POST'])
def resume():
    return render_template('index.html')

app.run(debug=True)