"""
One n*log(n)
- Quick sort and Merge Sort
- Know when to use merge over quick sort
"""

test_arrays = [
    [1, 10, 4, 2, 7, 3, 6, 9, 5, 8],  # Simple integers, 1-10, no repeats
    [1, 10, 4, 2, 3, 6, 9, 5, 8, 4, 2, 7],  # Simple integers, 1-10, repeats
    [-8, 5, 6, 3, 4, 8, 10, 0, -2],  # Simple integers, -10-10, repeats
    [-10, 7.9, 7, 5, -4, 3, 10, 9.9, 9.8333]   # floats, -10-10, repeats
]

print(test_arrays[0][:3])

def heap_sort():
    pass


def merge_sort(input_array):
    if input_array > 1:
        mid = int(len(input_array)/2)
        left_arr = input_array[:mid]
        right_arr = input_array[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        #Check left and right arrarys
        # make sure sure each array is empty



def quick_sort():
    pass


def bubble_sort():
    pass


def radix_sort():
    pass
