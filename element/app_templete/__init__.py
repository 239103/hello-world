#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

sys.path.append("app_templete");
sys.path.append("app_templete/views");
sys.path.append("app_templete/models");
from views import base