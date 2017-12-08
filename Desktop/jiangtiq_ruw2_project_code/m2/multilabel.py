import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer

import csv
import numpy
## apply cca to decrease demension
#X = CCA(n_components=2).fit(X, Y).transform(X)

mlb = MultiLabelBinarizer()

#tag=[['veterans-4','sexual-assault-2'],['clemency','health-care-3'],['health-care-3'],['donald-trump-en-us'],
#	['veterans-4', 'donald-trump-en-us'],['clemency'],['veterans-4', 'health-care-3'],['sexual-assault-2'],
#	['veterans-4'],['clemency', 'donald-trump-en-us']]
#y=mlb.fit_transform(tag)
tags = []
with open('tags.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        if len(line) == 0:
            tags.append(" ")
        tmp = line.split(', ')
        tags.append(tmp)
        
y=mlb.fit_transform(tags)
#['clemency', 'donald-trump-en-us', 'health-care-3', 'sexual-assault-2', 'veterans-4']
#texts=list(mlb.classes_)
#print texts

#dictionary = {k: v for v, k in enumerate(texts)}
#
#dictionary = corpora.Dictionary(texts)
#
#new_tag = "veterans-4 sexual-assault-2"
#new_vec = dictionary.doc2bow(new_tag.lower().split())
#print new_vec

X=numpy.load("vector.npy")
#
### binary array or sparse matrix 
#
#
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

classif = OneVsRestClassifier(SVC(kernel='linear'))

classif.fit(X_train, y_train)

accuracy=classif.score(X_test,y_test)

#X, Y = make_multilabel_classification(n_classes=4, n_labels=2,
#                                      allow_unlabeled=True,
#                                      random_state=1)
#
#X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.4,random_state=42)
#
#classif = OneVsRestClassifier(SVC(kernel='linear'))
#
#classif.fit(X_train, y_train)
#
#y_pd=classif.predict(X_test)
#
#accuracy=classif.score(X_test,y_test)