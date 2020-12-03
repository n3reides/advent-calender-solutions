import requests
import time
import copy


def main():
    URL = "https://adventofcode.com/2020/day/3/input"
    cookies = {
        'session': 'secret'
    }
    res = requests.get(URL, cookies=cookies)
    data = res.content.decode('UTF-8')
    matrix = [x for x in data.split('\n')[0:-1]]
    task_one(matrix)
    matrix = [x for x in data.split('\n')[0:-1]]
    task_two(matrix)


def repeat_pattern(factor: int, mat: [str]) -> [str]:
    i = 0
    while i <= len(mat) - 1:
        mat[i] += (mat[i] * factor)
        i += 1
    return mat


def task_one(matrix: [str]):
    print("Task 1:")
    tic = time.perf_counter()
    for i in range(len(matrix) - 1):
        matrix[i] = [j for j in matrix[i]]

    # Require: # columns >= (3 * # rows)
    # Hence multiply repeating columns by (# rows * 3) / # columns
    factor = (len(matrix) * 3 // len(matrix[0]))
    matrix = repeat_pattern(factor, matrix)

    j = 0
    counter = 0

    for i in range(len(matrix)):
        counter += 1 if (matrix[i][j] == '#') else 0
        j += 3
    toc = time.perf_counter()
    print("Time elapsed:", toc - tic, "secs")
    print("Trees found:", counter)
    print("-" * 50)


def task_two(matrix: [str]):
    print("Task 2:")
    tic = time.perf_counter()
    for i in range(len(matrix) - 1):
        matrix[i] = [j for j in matrix[i]]

    multipliers = [1, 3, 5, 7, 0.5]
    # First factor: Require # columns >= # rows -> factor = # rows / # cols
    # Second factor: Require # columns >= # rows * 3 -> factor = 3 * # rows / # cols
    # Third factor: Require # columns >= # rows * 5 -> factor = 5 * # rows / # cols
    # Fourth factor: Require # columns >= # rows * 7 -> factor = 7 * # rows / # cols
    # Fifth factor: Require # columns >= # rpws // 2 -> factor = 1/2 * # rows / # cols
    factors = [(len(matrix) * multipliers[0] // len(matrix[0])), (len(matrix) * multipliers[1] // len(matrix[0])),
               (len(matrix) * multipliers[2] // len(matrix[0])), (len(matrix) * multipliers[3] // len(matrix[0])),
               (int(len(matrix) * multipliers[4] // len(matrix[0])))]

    results = [None] * len(factors)
    for i in range(len(factors)):
        mat_clone = copy.deepcopy(matrix)
        repeated_matrix = repeat_pattern(factors[i], mat_clone)
        # print(len(repeated_matrix), len(repeated_matrix[0]))
        counter = 0
        k = 0

        for j in range(len(matrix)):
            if (i != 4):
                counter += 1 if (repeated_matrix[j][k] == '#') else 0
                k += multipliers[i]
            else:
                if k == 324:
                    break
                counter += 1 if (repeated_matrix[k][j] == '#') else 0
                k += 2
        results[i] = counter

    prod = 1
    for result in results:
        prod *= result

    toc = time.perf_counter()
    print("Time elapsed:", toc - tic, "secs")
    print("Total product found:", prod)
    print("-" * 50)


main()
