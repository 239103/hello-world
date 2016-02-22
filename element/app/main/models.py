# -*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash

import os, sys

class Jboss(object):
    '''Jboss application status'''
    Status = {} 
    
    def __init__(self, name):
        self.validate(name)
        
    def validate(self, name):
        self.Status = {'name': name,
                       'validation': False,
                       'basepath': '/app/jboss/jboss-as/server/' + name,
                       'deploypath': '/app/war/' + name,
                       'pidfile': '/app/jboss/jboss-as/logs/' + name + '.pid',
                       'pid' : 0,
                       }
        
        if os.path.exists(self.Status['basepath']):
            self.Status['validation'] = True
        
        '''
        if os.path.exists(self.Status['basepath']):
            if os.path.exists(self.Status['deploypath']):
                if os.path.exists(self.Status['pidfile']):
                    try:
                        with open(self.Status['pidfile']) as fd:
                            self.Status['pid'] = fd.readline()
                    except FileNotFoundError as e:
                        pass
                    if int(self.Status['pid']) > 0:
                        try:
                            os.getpid(self.Status['pid'])
                            self.Status['validation'] = True
                        except:
                            pass
        '''
    def __repr__(self):
        return self.Status