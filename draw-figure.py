import pylab as pl
import numpy as np

f3 = open("data.txt","r")

line = f3.readline()
linenum = 0
y_var = []
x_var = []
w_var = []
while 1 :
        if line :
                linenum +=1
                print "Line No.%d" %linenum

                line = line.strip()
                con = line.split(' ')
                y_var.append(1/float(con[0]))
                x_var.append((float(con[1])*float('1.80508055e-01') )+(float(con[2])* float('3.38783900e+01') )+ (float(con[3])*float('-1.18783433e+00') ) + (float(con[4])*float('-3.22622501e+03') ) + (float(con[5])* float('3.93560291e+00') ) + (float(con[6])*float('1.19577771e+05')) + (float(con[7]) * float('-7.38251418e+00')) + (float(con[8])* float('-1.97540706e+06') ) + (float(con[9])* float('8.41306977e+00') ) + (float(con[10]) *float( '1.60465754e+07')) + (float(con[11])* float('-6.07256929e+00') ) +(float(con[12])*float( '-6.45024772e+07')) + (float(con[13])*float( '2.83003649e+00')) + (float(con[14])* float('1.12428196e+08')) + (float(con[15]) *float( '-8.47718864e-01')) + (float(con[16])*float( '-2.94978691e+07')) + (float([17]) *float( '1.57397951e-01')) + (float(con[18])* float('-8.28336370e+07')) + (float(con[19])*float( '-1.64646418e-02')) + (float(con[20])*float( '-2.07955159e+07')) + (float(con[21])*float( '7.40792096e-04')) + (float(con[22])*float('7.10137493e+07'))-float('0.00501685466545') )
                #print"con[2]: %r"  %int(con[2])
        #       w_var.append(float(con[2]))
                i =1
        else :
                break
        line = f3.readline()
f3.close()
pl.plot(x_var,y_var,'o')
pl.show()
#pl.plot(w_var,y_var,'o')
#pl.show()
