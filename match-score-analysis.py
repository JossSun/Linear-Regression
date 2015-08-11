mport matplotlib.pyplot as plt

f1 = open("study.txt","r")
f2 = open("score.txt","w")
line = f1.readline()
score = []
big = []
while 1 :
        if line :
                con = line.split(' ')
                score.append(float(con[1]))
        else :
                break
        line = f1.readline()
count =0
for val in score :
        if val >1 :
                count +=1
                big.append(val)
                f2.write(str(val)+'\r\n')

        else :
                continue
big.sort()
print "score over '1' : %d " %count
print "max is : %r" %big[len(big)-1]
f1.close()
f2.close()
