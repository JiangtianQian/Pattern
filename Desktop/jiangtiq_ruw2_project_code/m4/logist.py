import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import csv
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
from sklearn.decomposition import PCA
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score 


#
#lines = np.loadtxt('combine.csv',dtype=np.str,delimiter=',')
#df = lines[0:,0:].astype('float')
#X = PCA(n_components=128).fit_transform(df)

lines = np.loadtxt('wordAfterCombine.csv',dtype=np.str,delimiter=',')
df = lines[0:,0:].astype('float')
X = df


y = []
with open('tagsAfterCombine.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        y.append(int(line[0]))
    
        

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

classify=LogisticRegression()


classify.fit(X_train, y_train)
y_pt=classify.predict(X_test)

accuracy=classify.score(X_test,y_test) 


#average_precision = average_precision_score(y_test, y_pt)

#precision, recall, _ = precision_recall_curve(y_test, y_pt)

macro_recall = recall_score(y_test, y_pt, average='macro') 
micro_recall = recall_score(y_test, y_pt, average='micro')


macro_precision = precision_score(y_test, y_pt, average='macro') 
micro_precision = precision_score(y_test, y_pt, average='micro')


