## Author: Olle Dahlstedt


import random
import time

randomlist = []
for i in range(0, 100000):
    n = random.randint(-40000, 40000)
    randomlist.append(n)


duplicates_removed = list(set(randomlist))
print("# unique nums between -10000 to 10000:", len(duplicates_removed))


def binary_search(counter: int, array: [int], key: int, low_idx: int, high_idx: int) -> int:
    mid_idx = low_idx + ((high_idx - low_idx) // 2)
    # print("#"*100)
    # print("iteration no.", counter, "key:", key, "high:", high_idx, "mid:", mid_idx, "low:", low_idx)
    while (mid_idx >= low_idx) and (mid_idx <= high_idx):
        if array[mid_idx] > key:
            return binary_search(counter=counter + 1, array=array, key=key, low_idx=low_idx, high_idx=mid_idx - 1)
        elif array[mid_idx] < key:
            return binary_search(counter=counter + 1, array=array, key=key, low_idx=mid_idx + 1, high_idx=high_idx)
        else:
            return mid_idx
    return -1


def n2log_threesum(array: [int]) -> []:
    tic = time.perf_counter()
    array.sort()
    tuple_list = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array) - 1):
            returned_index = binary_search(counter=0, array=array, key=(-1 * (array[i] + array[j])), low_idx=0,
                                           high_idx=len(array) - 1)
            if returned_index >= 0:
                tuple_list.append((array[i], array[j], array[returned_index]))
                toc = time.perf_counter()
                print("binary search threesum time elapsed:", toc - tic, "secs")
                return tuple_list

    toc = time.perf_counter()
    print("binary search threesum time elapsed:", toc - tic, "secs")
    return tuple_list


def threesum(array: [int]) -> []:
    tic = time.perf_counter()
    tuple_list = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array) - 1):
                if (array[i] + array[j] + array[k] == 0):
                    tuple_list.append((array[i], array[j], array[k]))
                    toc = time.perf_counter()
                    print("threesum time elapsed:", toc - tic, "secs")
                    return tuple_list

    toc = time.perf_counter()
    print("binary search threesum time elapsed:", toc - tic, "secs")
    return tuple_list


n2log_threesum(array=duplicates_removed)
threesum(array=duplicates_removed)
