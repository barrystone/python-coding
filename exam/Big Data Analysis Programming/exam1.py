import random


answer = input("請輸入班級人數:")

n = int(answer)
ary = []

for i in range(1,n+1):
    ary.append(i);
    for j in range(3):
        ary.append(random.randint(0,100))

numbers = [0]*n
avgNumbers = [0]*n
n2Idx=0;
for i in range(0,n):
    temp = []
    tempLen=0
    while tempLen<4:
        temp.append(ary[n2Idx])
        tempLen+=1
        n2Idx+=1
    tempSum=0
    for j in range(1,4):
        tempSum+=int(temp[j])
    temp.append(float('{:.1f}'.format(tempSum/3)))
    numbers[i] = temp[0:4]
    avgNumbers[i] = temp

cSum=0
mSum=0
eSum=0
for i in numbers:
    cSum+=int(i[1])
    mSum+=int(i[2])
    eSum+=int(i[3])
cAvg=0
mAvg=0
eAvg=0
cAvg=float('{:.1f}'.format(cSum/len(numbers)))
mAvg=float('{:.1f}'.format(mSum/len(numbers)))
eAvg=float('{:.1f}'.format(eSum/len(numbers)))


mathSortedNumbers =  avgNumbers.copy()
def sortMathFunc(e):
    return e[2]
mathSortedNumbers.sort(reverse=True,key=sortMathFunc)

mathGoodCount=0
mathGoodPeople=[]
mathBestPeoplePoint=mathSortedNumbers[0][2]
mathBestPeople=mathSortedNumbers[0][0]

for i in mathSortedNumbers:
    if (i[2]>=60) :
        mathGoodPeople.append(i[0])
        mathGoodCount+=1


sortedNumbers = avgNumbers.copy()
def sortItemFunc(e):
    return e[4]
sortedNumbers.sort(reverse=True,key=sortItemFunc)

print('成績列表(依據座號排序):')
print(' 座號   國文   數學   英文   平均')
for i in avgNumbers:
    print(' ',i[0] if (int(i[0]) >= 10) else f'{i[0]} ','  ',i[1],'  ',i[2],'  ',i[3],'  ',i[4])

print()

print("各科平均分數:")
print("國文 平均: ",cAvg)
print("數學 平均: ",mAvg)
print("英文 平均: ",eAvg)

print()

print("數學及格的人數: ",mathGoodCount)
print("數學及格的座號: " ,mathGoodPeople)
print("數學最高分: ",mathBestPeoplePoint) 
print("數學最高分的座號: ",mathBestPeople)

print()

print(' 座號   國文   數學   英文   平均')
for i in sortedNumbers:
    print(' ',i[0] if (int(i[0]) >= 10) else f'{i[0]} ','  ',i[1],'  ',i[2],'  ',i[3],'  ',i[4])
    