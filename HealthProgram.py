"""
input:

5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47

output:

16.2
172.4
63.0
15.8
164.4
51.6
A
"""
class HealthProgram():
    def __init__(self, ageList, heightList, weightList):
        self.ageList = ageList
        self.heightList = heightList
        self.weightList = weightList
    def ageMean(self):
        averageAge = 0
        for age in self.ageList:
            averageAge += age
        averageAge = averageAge /len(self.ageList)
        return averageAge

    def heightMean(self):
        averageHeight = 0
        for height in self.heightList:
            averageHeight += height
        averageHeight = averageHeight /len(self.heightList)
        return averageHeight

    def weightMean(self):
        averageWeight = 0
        for Weight in self.weightList:
            averageWeight += Weight
        averageWeight = averageWeight /len(self.weightList)
        return averageWeight

#school A
n = int(input())
ageLst = [float(x) for x in input().split()]
heightLst = [float(x) for x in input().split()]
weightLst = [float(x) for x in input().split()]

a = HealthProgram(ageLst, heightLst, weightLst)

#school B
n = int(input())
ageLstB = [float(x) for x in input().split()]
heightLstB = [float(x) for x in input().split()]
weightLstB = [float(x) for x in input().split()]

b = HealthProgram(ageLstB, heightLstB, weightLstB)

print(a.ageMean())
print(a.heightMean())
print(a.weightMean())

print(b.ageMean())
print(b.heightMean())
print(b.weightMean())

if a.heightMean() == b.heightMean():
    if a.weightMean() == b.weightMean():
        print("Same")
    elif a.weightMean() < b.weightMean():
        print("A")
    else:
        print("B")
elif a.heightMean() > b.heightMean():
    print("A")
else:
    print("B")