#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:41:44 2017

@author: joanluc
"""
import csv
file=open("dictionnaire_des_donnees.cvs","r")
test=csv.reader(file)
for row in test:
    print(row[1])