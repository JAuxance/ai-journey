import math
import numpy as np
import random
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
b = np.array([[1, 2, 3], [3, 5, 3]])
a = np.reshape(b, (3, 2))
print(a)
# convert 1D array to 2D array

# create new array
t = np.array([1, 2, 3, 4, 5, 6])
# ADD row
t2 = t[np.newaxis, :]
print(np.shape(t2))
print(t2)
print("-------------")
t2b = np.reshape(t2, (2, 3))
print(t2b)
# ADD column
t2 = t[:, np.newaxis]
print(t2)

# inserting a new axis at a specified position
y = np.array([1, 2, 3, 4, 5, 6])
y2 = np.expand_dims(y, axis=0)
print(np.shape(y2))
# slicing and indexing
o = np.array([[1, 2, 3, 4, 6, 4],
              [3, 4, 1, 31, 110, 45]])
print(o[1:2])
print("------------------------")
print(o[1, 2])
print("------------------------")
print(o[-4:])
three_up = (o >= 3)
print("------------------------")
print(o[three_up])
print("------------------------")
# mask
divisible_by_2 = o[o % 2 == 0]
print(divisible_by_2)
print("------------------")
mask_tf = (o < 2) | (o <= 5)
print(mask_tf)
list_of_cord = list(zip(o[0], o[1]))
for coord in list_of_cord:
    print(coord)
not_here = np.nonzero(o == 110)
print(not_here)

a3 = np.array([[1, 2],
              [1, 3]])

a4 = np.array([[11, 2],
              [31, 4]])
print("-----Vertical------")
stack_array_vertical = np.vstack((a3, a4))
print(stack_array_vertical)
print("-----Horizontal------")
stack_array_horizontal = np.hstack((a3, a4))
print(stack_array_horizontal)
print("-----Split-----")
p = np.arange(1, 29).reshape(4, 7)
print(p)
split_array = np.hsplit(p, (2, 4))
print(split_array)
# Array Operation
print("-----Operation-----\n Array of One plus random array")
g = np.arange(1, 11)
print("Array 0 to 10 -> {}".format(g))
rng = np.random.default_rng()
f = rng.choice(100, size=10, replace=False)
print("Random array -> {}".format(f))
print("Operation Result")
array_op_result = f // g
print(array_op_result)
h = rng.uniform(0, 0.70, size=(3, 4))
print("Array of < 1")
print(h)
print("-----UseFul array operation-----")
print("Sum of Column -> {}".format(h.sum(axis=0)))
print("Sum of Row -> {}".format(h.sum(axis=1)))
# Matrices Section
array_d2 = np.array([[1, 3], [4, 9], [2, 8]])
print("2D Array ->\n {}".format(array_d2))