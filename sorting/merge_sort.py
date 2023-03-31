# MergeSort
from typing import List


def mergeSort(arr: List[int]) -> None:

    if len(arr) <= 1:
        return
    mid_idx = len(arr) // 2
    # checkpoint 1: Here we don't need to create 2 new empty lists/arrays
    # and copy paste corresponding values to them as we usually do.
    # Notice that in Python slicing a list does not create a new object,
    # or in other word, generate copies of the objects in the lists. Slicing lists just copies the references to them.
    # But why modifying values in arr won't change values in left/right? Recall Python integer singletons!
    left = arr[:mid_idx]
    right = arr[mid_idx:]

    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    a = [2,3,7,5,55,23,9,0,22,16,23]
    print(a)
    mergeSort(a)
    print(a)
