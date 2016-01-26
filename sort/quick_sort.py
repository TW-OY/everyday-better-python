#!/usr/bin/env python
# encoding: utf-8


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left_arr = []
        right_arr = []
        pivot_index = int(len(arr) / 2)
        pivot = arr.pop(pivot_index)
        for item in arr:
            if item < pivot:
                left_arr.append(item)
            else:
                right_arr.append(item)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


def main():
    test_data = [1, 2, 5, 1, 3, 3, 53, 1, 23, 74, 62, 78, 1, 32, 23, 53, 23, 0, 0, 0, 0, 0]
    print quick_sort(test_data)


if __name__ == '__main__':
    main()
