import statsmodels.api as sm
import numpy as np
import pylab as pl
import math
from sklearn import metrics

f3 = open("data0.txt","r")
f2 = open("data.txt","w")
line = f3.readline()
linenum = 0

num = input()
while 1 :
	if line :
		linenum +=1
		print "Line No.%d" %linenum
		line = line.strip()
	        con = line.split(' ')
		s = 1/float(con[0])	
		n = pow(s,-1)-1
	        if n<=0 :
			pass
		else :
			m  = math.log(n)
			num0 = (-1) *m 
			
		num1 = float(con[1])
		num2 = 1/float(con[2])
		f2.write(str(num0))
		i =1
		while (i<=num) :
			tmp1 = pow(num1,i)
			tmp2 = pow(num2,i)
			f2.write(' '+str(tmp1)+' '+str(tmp2))
			i +=1
		f2.write('\r\n')
 
	else :
		break
	line = f3.readline()

f2.close()
f3.close()

#start to regression
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#Load in train data
f1 = open("data.txt")
f4 = open("result.txt","w")
data = np.loadtxt(f1)
X = data[:,1:] #load in colomn 1 and colomn 2
y = data[:,0]

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)


#Fit in the model
linreg = LinearRegression()
linreg.fit(X_train,y_train)

y_pred = linreg.predict(X_test)

print linreg.intercept_
print linreg.coef_
print "MSE : ",metrics.mean_squared_error(y_test,y_pred)
f4.write(str(linreg.intercept_)+' ')
f4.write(str(linreg.coef_))


f1.close()
f4.close()
