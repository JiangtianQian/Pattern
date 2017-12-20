import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import csv


lines = np.loadtxt('combine.csv',dtype=np.str,delimiter=',')
df = lines[0:,0:].astype('float')
X = PCA(n_components=128).fit_transform(df)


y = []
with open('tagsAfterCombine.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        if len(line[0]) == 0:
            tags.append(" ")
        y.append(int(line[0]))
    
        

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

classify=LogisticRegression()

classify.fit(X_train, y_train)

accuracy=classify.score(X_test,y_test) 