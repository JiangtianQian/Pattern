import numpy as np
lines = np.loadtxt('test.csv',delimiter=',',dtype='str')
X = lines[1:,1:25].astype('double')
Y = lines[1:,25].astype('double')
