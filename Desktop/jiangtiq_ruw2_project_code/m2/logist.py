import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing



lines = np.loadtxt('karate.csv',delimiter=',',dtype='str')

 
X = lines[1:,1:25].astype('double')
y = lines[1:,25].astype('double')     

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

classify=LogisticRegression()

classify.fit(X_test, y_test)

accuracy=classify.score(X_test,y_test)