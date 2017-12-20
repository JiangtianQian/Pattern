#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import numpy
import numpy as np

featureWord = {}
add = {}
X=numpy.load("vec.npy")
i = 0
with open('feature20.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        featureWord[line[0]] = X[i]
        i = i+ 1
        
tmp = np.loadtxt("karate1.csv", dtype=np.str, delimiter=",")
data = tmp[0:,0:].astype(np.float)
j = 0
with open('petitionNId.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        add[line[0]] = data[j]
        j = j + 1
        
for key in add:
    if featureWord.has_key(key):
        if len(add[key]) != 0:
            addTmp = np.column_stack((featureWord[key],add[key])).reshape(-1)
            featureWord[key] = addTmp
        
with open('combine.csv', 'w') as csvfile:
    fieldnames = ['ids', 'feature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in featureWord:
        if len(featureWord[i]) > 128:
            write_dict = {}
            write_dict['ids']= i
            write_dict['feature'] = ','.join(str(x) for x in featureWord[i])
            writer.writerow(write_dict)
        


print "done"

