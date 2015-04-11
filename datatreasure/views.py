from flask import render_template, url_for, redirect, flash, send_from_directory
from datatreasure import datatreasure
import os
import json

@datatreasure.route('/')
@datatreasure.route('/home')
@datatreasure.route('/home/')
def index():
    return "Hi!"
