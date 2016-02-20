# -*- coding:utf-8 -*-

from . import extra

@extra.route('/extra')
def extra_index():
    return "This is EXTRA instance.\n"