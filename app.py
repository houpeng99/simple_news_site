#!/usr/bin/env  python3
from flask import Flask, render_template, url_for, redirect, abort, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    path = '/home/shiyanlou/files/'
    files = os.listdir(path)
    titles = []
    for file in files:
        filename = path + file
        with open(filename) as f:
            json_dict = json.load(f)
            title = json_dict['title']
        titles.append(title)
    return render_template('index.html', titles=titles)


@app.route('/files/<filename>')
def file(filename):
    dirpath = '/home/shiyanlou/files/'
    filepath = os.path.join(dirpath, filename + '.json')
    if not os.path.exists(filepath):
        abort(404)
    else:
        info = []
        with open(filepath) as f:
            json_dict = json.load(f)
            print('jsdict', json_dict)
            info.append(json_dict)
        return render_template('file.html', info=info)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__ == "__main__":
    app.run(debug=True)
