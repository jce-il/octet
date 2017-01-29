#!/usr/intel/bin/python3.3.1
# -*- coding: utf-8 -*-

class ICQ:
# name           - the name of the quantity
# unit           - the unit in which the quantity is measured
# val            - the value of the quantity
# lowerB, upperB - the lower and upper boundaries of the quantity

    def valid(val,u,l):
        if u = -1:
            if l = -1:
                return 1
            else:
                if val>= l:
                    return 1
                else:
                    return 0
        else:
            if l=-1:
                if val <= u:
                    return 1
                else:
                    return 0
            else:
                if val >= l and val <= u:
                    return 1
                else:
                    return 0

    def __init__(self,name):
        self.name   = name
        self.lowerB = -1
        self.upperB = -1
        self.val    = None
        self.unit   = None
        
    def __init__(self,name,value,un=None,l=None,u=None):
        self.name   = name
        self.lowerB = l
        self.upperB = u
        self.unit   = un 
        if valid(val,u,l):
            self.val = value
        else:
            self.val = None
    
    def increase(self,byhowmuch):
        if self.val is None and valid(byhowmuch,u,l):
            self.val = byhowmuch
        elif self.val is not None and valid(val+byhowmuch,u,l):
            self.val += byhowmuch

    def setLower(self,l):
        if self.val is None and self.upperB is None:
            self.lowerB = l
            return
        if self.val is None and self.upperB >= l:
            self.lowerB = l
            return
        if self.val >= l:
            self.lowerB = l
            return

   def setUpper(self,u):
        if self.val is None and self.lowerB is None:
            self.upperB = u
            return
        if self.val is None and self.lowerB <= u:
            self.upperB = u
            return
        if self.val <= l:
            self.upperB = u
            return
def mkDensity(value):
    if value >0:
        return ICQ('density', value, 'kg/m3',0)
def mkKTemperature(value):
    if value>=0:
        return ICQ('temperature', value, 'degree',0)
def mkCTemperature(value):
    if value>=-273:
        return ICQ('temperature', value, 'degree',-273)
def mkBoilingPnt(value):
    return ICQ('boiling point',value,'degree')
def mkMeltingPnt(value):
    return ICQ('melting point',value,'degree')
def mkConcentration(value):
    if value>=0 and value <=100:
        return ICQ('concentration',value,'percent',0,100)
def mkMolality(value):
    return mkConcentration(value)
def mkPresure(value):
    if value >= 0:
        return ICQ('pressure',value,'pascal',0)




