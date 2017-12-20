#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:46:48 2017

@author: kaka
"""

import csv

l = []
with open('node.csv') as nodefile:
    for row in nodefile:
        l.append(row)


#write_dic = {}
#with open('labelresult.csv', 'w') as csvfile:
#    fieldnames = ['source','target', 'label']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    
#    with open('label1.csv') as f:
#        f1 = csv.reader(f)
#        for row in f1:
#            if (row[0] == "U3893") | (row[1] == "U3893"):
#                write_dic['source'] = row[0]
#                write_dic['target'] = row[1]
#                write_dic['label'] = row[2]
#                writer.writerow(write_dic)
            
print "done"