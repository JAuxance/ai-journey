import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array_3d = np.array([
    [
        [1, 3, 4],
        [4, 3, 3],
        [2, 3, 2]
    ]
])

print(f"Shape of a: {a.shape}")
print(f"Number of dimensions of a: {a.ndim}")

copy_array = np.copy(a)
copy_array[0, 0] = 50

print("\nOriginal array a:")
print(a)

print("\nIndependent copy:")
print(copy_array)

print(f"\nlen(a.shape) = {len(a.shape)}")
print(f"a.ndim = {a.ndim}")
print(f"len(a.shape) == a.ndim -> {len(a.shape) == a.ndim}")

print(f"\nShape of array_3d: {array_3d.shape}")
print(f"Number of dimensions of array_3d: {array_3d.ndim}")
print(f"len(array_3d.shape) == array_3d.ndim -> {len(array_3d.shape) == array_3d.ndim}")
