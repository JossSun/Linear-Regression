import matplotlib.pyplot as plt

f1 = open("study.txt","r")
f2 = open("sort-real-rank.txt","w")
line = f1.readline()
rank = []
while 1 :
        if line :
                con = line.split(' ')
                rank.append(int(con[2]))
        else :
                break
        line = f1.readline()

rank.sort()
f2.write(str(rank))
min = rank[0]
max = rank[len(rank)-1]
print "min:%s" %min
print "max:%s" %max
f1.close()
f2.close()

f3 = open("chart.txt","w")
iter = 1
count = []
value =0
count = [value]*30
print count

for val in rank :
        if val < 10000*iter and val >= 10000*(iter-1):
                count[iter-1] += 1
        else :
                iter +=1
                count[iter-1] +=1

print "count is :"
print count
f3.write(str(count))

f3.close()

plt.bar(left = (100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000), height =(300140, 142209, 100534, 80403, 68190, 58958, 52753, 45220, 41805, 39087, 36057, 34954, 34319, 32862, 30182, 27604, 26099, 24162, 24404, 22369, 20118, 20407, 19909, 19658, 47), width = 300 )
plt.show()

bar = []
i = 0
while (i<30) :
        bar.append( 10000*i)
        i +=1

plt.bar(left = bar, height = count, width = 6000)
plt.show()
