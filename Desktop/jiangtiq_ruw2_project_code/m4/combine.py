#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import numpy
import numpy as np

featureWord = {}
add = {}
X=numpy.load("word_vec.npy")
i = 0
tags = {}
with open('vic_des.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        featureWord[line[0]] = X[i]
        tags[line[0]] = line[2]
        i = i+ 1
        
tmp = np.loadtxt("UserNetwork.csv", dtype=np.str, delimiter=",")
data = tmp[0:,0:].astype(np.float)
j = 0
with open('node_ID.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        add[line[0]] = data[j]
        j = j + 1
 
tag = {}  
f = {}     
for key in add:
    if featureWord.has_key(key):
        if len(add[key]) != 0:
            f[key] = featureWord[key]
            addTmp = np.column_stack((add[key],featureWord[key])).reshape(-1)
            featureWord[key] = addTmp
            tag[key] = tags[key]


with open('combine.csv', 'w') as csvfile:
    fieldnames = ['ids', 'feature','tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in featureWord:
        if len(featureWord[i]) > 128:
            write_dict = {}
            write_dict['ids']= i
            write_dict['feature'] = ','.join(str(x) for x in featureWord[i])
            write_dict['tags'] = tag[i]
            writer.writerow(write_dict)
            
with open('wordAfterCombine.csv', 'w') as csvfile:
    fieldnames = ['ids', 'feature','tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in f:
        write_dict = {}
        write_dict['ids']= i
        write_dict['feature'] = ','.join(str(x) for x in f[i])
        write_dict['tags'] = tag[i]
        writer.writerow(write_dict)
        


print "done"

