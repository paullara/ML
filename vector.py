import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([4, -1, 2])
d = np.array([-2, 3, 1])

vector_addition = a + b

dot_product = np.dot(a,b)

print(vector_addition, dot_product)

vector_subtraction = a - b
print("Subtraction of a and b:", vector_subtraction)

d_product = np.dot(c, d)
print("Dot product of a and b:", d_product)

cross_product = np.cross(c, d)
print("Cross product of a and b:", cross_product)

