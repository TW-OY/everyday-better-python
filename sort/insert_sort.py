#!/usr/bin/env python
# encoding: utf-8


def insert_sort(arr):
    sorted_arr = []
    sorted_arr.append(arr[0])
    for index_a in range(1, len(arr)):
        if arr[index_a] >= sorted_arr[len(sorted_arr) - 1]:
            sorted_arr.append(arr[index_a])
        else:
            for index_b in range(len(sorted_arr)):
                if arr[index_a] <= sorted_arr[index_b]:
                    sorted_arr.insert(index_b, arr[index_a])
                    break
    return sorted_arr


def main():
    test_data = [1, 2, 5, 1, 3, 3, 53, 1, 23, 74, 62, 78, 1, 32, 23, 53, 23, 0, 0, 0, 0, 0]
    print insert_sort(test_data)


if __name__ == '__main__':
    main()
