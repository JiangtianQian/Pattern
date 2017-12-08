#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:20:03 2017

@author: kaka
"""

import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import f1_score
from sklearn.decomposition import PCA

import csv
import numpy
import re
mlb = MultiLabelBinarizer()

tags = []
with open('tagsNew.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        if len(line[0]) == 0:
            tags.append(" ")
        tmp = line[0][1:len(line[0]) - 1]
        p = re.compile(r"'")
        tmp = p.sub('',tmp)
        p = re.compile(r'"')
        tmp = p.sub('',tmp)
        tmp = tmp.split(', ')
        tags.append(tmp)

y=mlb.fit_transform(tags)


#lines = np.loadtxt('combine.csv',delimiter=',',dtype='str')
#df = lines[1:,:4].astype('float')

#X = PCA(n_components=128).fit_transform(lines)

X=numpy.load("vec.npy")
#
### binary array or sparse matrix 
#
#
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

classif = OneVsRestClassifier(SVC(kernel='linear'))

classif.fit(X_train, y_train)


y_pt=classif.predict(X_test)
micro = 0
macro = 0
for i in range(len(y_test)):
    micro = micro + f1_score(y_test[i],y_pt[i],average =  'micro')
    macro = macro + f1_score(y_test[i],y_pt[i],average =  'macro')
aveMicro = micro / len(y_test)
aveMacro = macro / len(y_test)

