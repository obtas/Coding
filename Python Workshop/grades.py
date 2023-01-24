data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

newdata=data.split(",")

numarray = []

for x in newdata:
    convdata= int(x)
    numarray.append(convdata)
print(numarray)
    

print("---------------------------------")

minnum = min(numarray)
maxnum = max(numarray)

print(minnum)
print(maxnum)

print("---------------------------------")

sum = sum(numarray)
print(sum)
len = len(numarray)
print(len)
avgdata= sum / len
print(avgdata)

rounded =round(avgdata, 2)
print(rounded)

print("---------------------------------")
import statistics

stats = statistics.mean(numarray)
print(round(stats,2))

med = statistics.median(numarray)
print(med)

print("---------------------------------")

datasum = "The minimum of the data is {minnum} max is {maxnum}. The average is {rounded}, the mean is {stats} and the median is {med}".format(minnum,maxnum,rounded,stats,med)


