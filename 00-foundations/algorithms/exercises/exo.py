import numpy as np

# Exo 1


def array_stats():
    a = np.array([[2, 4, 6], [1, 3, 5]])
    print(a.shape)
    print(a.ndim)
    print(a.size)
    print(a.dtype)

# Exo 2


def array_copy():
    original = np.arange(10)
    copy = np.copy(original)
    print(f"original - >\n{original}\ncopy - >\n{copy}")

# Exo 3


def diff_array():
    range_array = np.arange(15)
    minispace_array = np.linspace(0, 1, num=5)
    array_of_ones = np.ones((2, 3), dtype=np.int64)
    empty_array = np.empty(4)
    print(f"{range_array}\n{minispace_array}\n{array_of_ones}\n{empty_array}")
# Exo 4


def sort_and_add():
    x = np.array([9, 2, 7, 2, 1], dtype=np.int64)
    x.sort(kind='quicksort')
    array = np.array([100, 200], dtype=np.int64)
    concat_array = np.concat((x, array))
    print(concat_array)
# Exo 5


def Reshape():
    b = np.arange(1, 13)
    print(b.reshape(3, 4))
    print(b.reshape(2, 6))
    print("On ne peux pas reshape car il n'y a pas un montent qui convient pour le reshape(5, 3)")
# Exo 6


def line_col_axis():
    t = np.array([10, 20, 30, 40])
    t = t.reshape(2, 2)
    new_row_version = t[np.newaxis, :]
    new_col_version = t[:, np.newaxis]
    print(
        f"Row array - >\n{new_row_version}\nCal array - >\n{new_col_version}\n")

    row = np.expand_dims(t, axis=0)
    col = np.expand_dims(t, axis=1)
    print(f"{row}\n")
    print(f"{col}\n")
# Exo 7


def index_slicing():
    c = np.array([[1, 2, 3, 4],
                  [10, 20, 30, 40]])
    print(c[1, 2])
    print(c[: 1])
    print(c[1:])
    print(c[:, 1])


# Exo 8


def mask():
    d = np.array([[1, 8, 3], [4, 11, 6]])
    five_mask = d >= 5
    peer_mask = d % 2 == 0
    print(f"Mask of 5 - >\n{d[five_mask]}\n")
    print(f"Peer Mask - >\n{d[peer_mask]}\n")
    print(np.nonzero(d == 6))
# Exo 9


def matrices():
    m1 = np.arange(4).reshape(2, 2)
    m2 = np.arange(4).reshape(2, 2)
    m1_vstack = np.vstack((m1, m2))
    m1_hstack = np.hstack((m1, m2))
    print(f"Vertical stack - >\n{m1_vstack}\n")
    print(f"Horizontal stack - >\n{m1_hstack}\n")
    print("On vois qu vstack stack les valeur sur l'axe vertical mais hstack lui les stack sur l'axe Horizontal")
    print(np.shape(m1_vstack))
    print(np.shape(m1_hstack))

def main():
    array_stats()
    array_copy()
    diff_array()
    sort_and_add()
    Reshape()
    line_col_axis()
    index_slicing()
    mask()
    matrices()

if __name__ == "__main__":
    main()