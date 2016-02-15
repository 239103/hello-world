#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app_templete import app
from flask import render_template

@app.route('/')
def index():
    return "Hello World!\n"