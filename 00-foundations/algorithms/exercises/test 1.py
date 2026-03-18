import math
import numpy as np
a = np.array([[1, 2, 4, 5], [4, 2, 3, 1], [1, 29, 200, 23]])


print(a.shape)

print(a.size)

if a.size == math.prod(a.shape):
    print("The size of a is equal to the product of its shape. Plot twist: this should never be false.")
else:
    print("The size of a is not equal to the product of its shape.")

# Dtype attribute
print(a.dtype)

# Create some type of array
array_0 = np.empty(3)
print(array_0)
array_1 = np.arange(200)
print(array_1)
array_lnp = np.linspace(10, 100, num=20)
print(array_lnp)
array_of_dtype = np.ones(3, dtype=np.int64)
print(array_of_dtype)
unsorted_array = np.array([1, 3, 222, 4, 1, 3])
print(np.sort(unsorted_array, kind="quicksort"))
print(np.concatenate((array_lnp, array_of_dtype)))

y = np.array([[1, 2], [3, 4]])
x = np.array([[5, 3]])
print(np.concatenate((y, x)))