import math
import numpy as np


LINE_WIDTH = 68


def page_title(title):
    print("\n" + "=" * LINE_WIDTH)
    print(title.upper().center(LINE_WIDTH))
    print("=" * LINE_WIDTH)


def section(title):
    print(f"\n[ {title} ]")
    print("-" * LINE_WIDTH)


def show_array(name, array):
    print(f"{name} -> shape={array.shape}, ndim={array.ndim}, dtype={array.dtype}")
    print(array)


# NumPy topics:
# - Array fundamentals
# - Array attributes
def basics_section():
    section("1. Basics")

    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    array_3d = np.array([[[1, 3, 4], [4, 3, 3], [2, 3, 2]]])
    array_a = np.array([[1, 2, 4, 5], [4, 2, 3, 1], [1, 29, 200, 23]])

    show_array("array_2d", array_2d)
    print(f"size={array_2d.size}")
    print(f"len(shape) == ndim -> {len(array_2d.shape) == array_2d.ndim}")

    print()
    show_array("array_3d", array_3d)
    print(f"size={array_3d.size}")
    print(f"len(shape) == ndim -> {len(array_3d.shape) == array_3d.ndim}")

    print()
    show_array("array_a", array_a)
    print(f"size={array_a.size}")
    print(
        f"I see that size == product of shape -> {array_a.size == math.prod(array_a.shape)}")


# NumPy topic:
# - How to create an array from existing data
def copy_section():
    section("2. Copy")

    original = np.array([[1, 2, 3], [4, 5, 6]])
    copied = np.copy(original)
    copied[0, 0] = 50

    show_array("original", original)
    print()
    show_array("copied", copied)
    print(
        f"I can change the copy without changing the original -> {original[0, 0] == 1}")


# NumPy topics:
# - How to create a basic array
# - Adding, removing, and sorting elements
def creation_section():
    section("3. Array Creation")

    empty_array = np.empty(3)
    range_array = np.arange(12)
    line_array = np.linspace(10, 100, num=6)
    ones_array = np.ones(3, dtype=np.int64)
    unsorted_array = np.array([1, 3, 222, 4, 1, 3])

    show_array("np.empty(3)", empty_array)
    print()
    show_array("np.arange(12)", range_array)
    print()
    show_array("np.linspace(10, 100, 6)", line_array)
    print()
    show_array("np.ones(3, dtype=np.int64)", ones_array)
    print()
    show_array("np.sort(...)", np.sort(unsorted_array, kind="quicksort"))
    print()
    show_array("concat(line_array, ones_array)",
               np.concatenate((line_array, ones_array)))


# NumPy topics:
# - Can you reshape an array?
# - How to convert a 1D array into a 2D array
# - Transposing and reshaping a matrix
def reshape_section():
    section("4. Reshape And Axes")

    array_y = np.array([[1, 2], [3, 4]])
    array_x = np.array([[5, 3]])
    concatenated = np.concatenate((array_y, array_x))

    array_b = np.array([[1, 2, 3], [3, 5, 3]])
    reshaped_b = np.reshape(array_b, (3, 2))

    array_t = np.array([1, 2, 3, 4, 5, 6])
    row_version = array_t[np.newaxis, :]
    column_version = array_t[:, np.newaxis]
    expanded_axis = np.expand_dims(array_t, axis=0)

    show_array("concatenate(y, x)", concatenated)
    print()
    show_array("reshape(b, (3, 2))", reshaped_b)
    print(
        f"I see that reshape keeps the same total number of elements -> {array_b.size == reshaped_b.size}")

    print()
    show_array("1D -> row with newaxis", row_version)
    show_array("1D -> column with newaxis", column_version)
    show_array("expand_dims(axis=0)", expanded_axis)


# NumPy topic:
# - Indexing and slicing
def indexing_section():
    section("5. Indexing Slicing Masks")

    array_o = np.array([[1, 2, 3, 4, 6, 4], [3, 4, 1, 31, 110, 45]])
    mask_three_or_more = array_o >= 3
    even_values = array_o[array_o % 2 == 0]
    combined_mask = (array_o < 2) | (array_o <= 5)
    pairs = list(zip(array_o[0], array_o[1]))
    position_110 = np.nonzero(array_o == 110)

    show_array("array_o", array_o)
    print(f"array_o[1:2] ->\n{array_o[1:2]}")
    print(f"array_o[1, 2] -> {array_o[1, 2]}")
    print(f"array_o[-4:] ->\n{array_o[-4:]}")

    print()
    print("Mask array_o >= 3 ->")
    print(mask_three_or_more)
    print("Values where array_o >= 3 ->")
    print(array_o[mask_three_or_more])

    print()
    print("Values divisible by 2 ->")
    print(even_values)
    print("Combined mask ->")
    print(combined_mask)
    print("Pairs built from the two rows ->")
    print(pairs)
    print(f"Position of 110 -> {position_110}")


# NumPy topic:
# - How to create an array from existing data
def stack_split_section():
    section("6. Stack And Split")

    array_a3 = np.array([[1, 2], [1, 3]])
    array_a4 = np.array([[11, 2], [31, 4]])
    array_p = np.arange(1, 29).reshape(4, 7)

    show_array("vstack(a3, a4)", np.vstack((array_a3, array_a4)))
    print()
    show_array("hstack(a3, a4)", np.hstack((array_a3, array_a4)))
    print()
    show_array("array_p", array_p)
    print("hsplit(array_p, (2, 4)) ->")
    for index, part in enumerate(np.hsplit(array_p, (2, 4)), start=1):
        print(f"part {index}:")
        print(part)


# NumPy topics:
# - More useful array operations
# - Creating matrices
# - Generating random numbers
# - How to get unique items and counts
# - Transposing and reshaping a matrix
# - How to reverse an array
def operations_section():
    section("7. Operations And Matrices")

    rng = np.random.default_rng(42)

    array_g = np.arange(1, 11)
    array_f = rng.choice(100, size=10, replace=False)
    array_h = rng.uniform(0, 0.70, size=(3, 4))
    array_d2 = np.array([[1, 3], [4, 9], [2, 8]])
    random_matrix = rng.integers(1, 10, size=(3, 2), endpoint=True)
    array_l = np.array([11, 11, 12, 13, 14, 15, 16,
                       17, 12, 13, 11, 14, 18, 19, 20])
    array_24 = rng.integers(1, 100, size=24)
    matrix_4col = array_24.reshape(6, 4)

    show_array("array_g", array_g)
    print()
    show_array("array_f", array_f)
    print("array_f // array_g ->")
    print(array_f // array_g)

    print()
    show_array("array_h", array_h)
    print(f"sum of columns -> {array_h.sum(axis=0)}")
    print(f"sum of rows -> {array_h.sum(axis=1)}")

    print()
    show_array("array_d2", array_d2)
    print()
    show_array("random_matrix", random_matrix)
    print("transpose(random_matrix) ->")
    print(random_matrix.T)

    print()
    unique_values, first_positions = np.unique(array_l, return_index=True)
    print(f"unique values -> {unique_values}")
    print(f"first positions -> {first_positions}")

    print()
    show_array("matrix_4col", matrix_4col)
    print("np.flip(matrix_4col, axis=1) ->")
    print(np.flip(matrix_4col, axis=1))


def flattening_arrays_section():
    section("8. Reshaping and flattening multidimensional arrays")

    print()
    array_a = np.arange(0, 15).reshape(3, 5)
    show_array("Original array", array_a)
    array_flatten = array_a.flatten()
    array_flatten[0] = 100
    print()
    print(f"Flattened with \"flatten\" ->\n{array_flatten}")
    print()
    show_array("Original array", array_a)
    print()
    print("I can see that \"flatten\" does not change the original array.")

    print()
    array_c = np.arange(0, 15).reshape(3, 5)

    show_array("Original array", array_c)
    array_ravel = array_c.ravel()
    array_ravel[0] = 100

    print()
    print(f"Flattened with \"ravel\" ->\n{array_ravel}")
    print()
    show_array("Original array", array_c)
    print()
    print("In this example, I can see that \"ravel\" changes the original array.")


def main():
    page_title("My NumPy Journal")
    basics_section()
    copy_section()
    creation_section()
    reshape_section()
    indexing_section()
    stack_split_section()
    operations_section()
    flattening_arrays_section()


if __name__ == "__main__":
    main()
