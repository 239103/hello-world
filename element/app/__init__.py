#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

sys.path.append("app");
sys.path.append("app/views");
sys.path.append("app/models");
from views import base