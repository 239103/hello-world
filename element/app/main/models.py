# -*- coding:utf-8 -*-

import os

class Jboss(object):
    '''Jboss application status'''
    Status = {'name': '',
              'validation': False,
              'basepath': '',
              'deploypath': '',
              'pidfile': '',
              'pid' : 0,
              }    
    
    def __init__(self, name):
        '''initialize parameters'''
        self.Status['validation'] = False
        self.Status['name'] = name
        self.Status['basepath'] = '/app/jboss/jboss-as/server/' + name
        self.Status['deploypath'] = '/app/war/' + name
        self.Status['pidfile'] = '/app/jboss/jboss-as/logs/' + name + '.pid'        
        self.Status['pid'] = 0
        
        '''validate parameters'''
        self.validate(name)
        
    def validate(self, name):
        if os.path.exists(self.Status['basepath']):
            if os.path.exists(self.Status['deploypath']):
                if os.path.exists(self.Status['pidfile']):
                    try:
                        with open(self.Status['pidfile']) as fd:
                            pid = fd.readline()
                            self.Status['pid'] = int(pid.strip())
                    except FileNotFoundError as e:
                        pass
                    if self.Status['pid'] > 0:
                        try:
                            if os.getpgid(self.Status['pid']) > 0:
                                self.Status['validation'] = True
                        except:
                            pass
        
    def __repr__(self):
        return self.Status
    