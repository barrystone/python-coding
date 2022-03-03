import numpy as np

# Array 陣列

np1 = np.array([1,2,3])
np2 = np.array([4,5,6])

print(np1+np2)
print(np1.ndim, np1.shape, np1.dtype)


np3 = np.array([1,2,3,4,5,6])
np3 = np3.reshape([2,3])

print(np3.ndim, np3.shape, np3.dtype)

np3 = np3.astype('int32')
print(np3.dtype)


npZero = np.zeros([2,3])
npOne = np.ones([2,3])


print('布林遮罩')
np4 = np.array([1,2,3,4,5,6])
print(np4 > 3)
print(np4[np4 > 3])

print('元素加總')
np4 = np4.reshape([2,3])
print(np3.sum(axis= 1))
print(np3.sum(axis= 0))


