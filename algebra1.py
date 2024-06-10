import numpy as np 

x = np.array([1, 2, 3, 4])
A = np.array([[1, 2, 4], [3, 4, 4], [5, 6, 4], [7, 8, 4]])
B = np.array([[2, 4, 5], [4, 6, 6], [7, 9, 10], [8, 9, 10]])
A_t = A.T
B_t = B.T
C = A + B

print(A.shape)
print(A_t)
print('after A')
print(B_t)
print(B.shape)
print(B_t.shape)
print(A_t.shape)
print(x.shape)
print(C)


