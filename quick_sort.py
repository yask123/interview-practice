"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    less = []
    equal = []
    more = []

    if len(array)>1:
        pivot = array[-1]

        for each in array:
            if each < pivot:
                less.append(each)
            elif each == pivot:
                equal.append(each)
            else:
                more.append(each)

        return quicksort(less)+equal+quicksort(more)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
