# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:42:01 2020

@author: c00221719
"""

import os
from flask import Flask, render_template, request 

app = Flask(__name__)

#roots
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/") #domain name

def index():
    return render_template("upload.html")# -*- coding: utf-8 -*-

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
        
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)