import numpy as np
print("第一部分")
n  = int(input("請輸入n＝"))

arrayA = np.ones((n,n),dtype=int)
idx = 0
for i in arrayA:
    i+=idx
    idx+=1

print("Array_a:")
print(arrayA)

arrayB = np.random.randint(-100,100,size=[n,n])
print("Array_b:")
print(arrayB)

np.savetxt('array_a.txt',arrayA,delimiter=",")
np.savetxt('array_b.txt',arrayB,delimiter=",")

