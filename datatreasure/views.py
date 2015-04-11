from flask import render_template, url_for, redirect, flash, send_from_directory, request
from datatreasure import datatreasure
import os
import json

@datatreasure.route('/')
@datatreasure.route('/home')
@datatreasure.route('/home/')

def index():
    return render_template("home.html")

@datatreasure.route('/search', methods=['POST'])

def search():
  keyword = request.form['keyword']
