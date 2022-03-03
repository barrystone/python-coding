import numpy as np

print("第二部分")

arrayA = np.loadtxt("array_a.txt",delimiter=",")
arrayB = np.loadtxt("array_b.txt",delimiter=",")
arrayC = arrayA @ arrayB

print("Array_a:")
print(arrayA)
print("Array_b:")
print(arrayB)
print("Array_c:")
print(arrayC)

np.savetxt('array_c.txt',arrayC,delimiter=",")

