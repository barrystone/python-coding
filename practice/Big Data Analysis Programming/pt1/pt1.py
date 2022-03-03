file1 = open("ex1-input.txt", "r")
content = file1.read()
#print(content)

# 標題串列
titles = content.split('\n')[0].split(',')

ary1 = content.split('\n')
ary2 = ary1[1:len(ary1)-1]
allNumbers = [0]*len(ary2*4)


# Split all of numbers
n1Idx=0
for i in range(0,len(ary2)):
    for j in range(0,4):
        allNumbers[n1Idx] = ary2[i].split(',')[j]
        n1Idx+=1

print('allNumbers',allNumbers)


# 數值串列 / 數值串列(加上平均)
numbers = [0]*len(ary2)
avgNumbers = [0]*len(ary2)
n2Idx=0;
for i in range(0,len(ary2)):
    temp = []
    tempLen=0
    while tempLen<4:
        temp.append(allNumbers[n2Idx])
        tempLen+=1
        n2Idx+=1
    tempSum=0
    for j in range(1,4):
        tempSum+=int(temp[j])
    temp.append(float('{:.1f}'.format(tempSum/3)))
    numbers[i] = temp[0:4]
    avgNumbers[i] = temp

# 各科平均分數
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

# 依平均分數遞減排序
sortedNumbers = avgNumbers
def sortItemFunc(e):
    return e[4]
sortedNumbers.sort(reverse=True,key=sortItemFunc)


print("標題串列:")
print(titles)
print("數值串列:")
print(numbers)
print("數值串列(加上平均):")
print(avgNumbers)
print('')
print("各科平均分數:")
print("國文 平均: ",cAvg)
print("數學 平均: ",mAvg)
print("英文 平均: ",eAvg)
print('')
print("依平均分數遞減排序:")
print(' 座號   國文   數學   英文   平均')
for i in sortedNumbers:
    print(' ',i[0] if (int(i[0]) >= 10) else f'{i[0]} ','  ',i[1],'  ',i[2],'  ',i[3],'  ',i[4])



file1.close()

