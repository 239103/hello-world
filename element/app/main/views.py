#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import main
from .. import db
from . import models

@main.route('/')
def index():
    return "Hello World!\n"