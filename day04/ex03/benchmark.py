#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

# Функция для вычисления суммы квадратов с использованием цикла
def sum_of_squares_loop(nsum):
    sum = 0
    for i in range(1, nsum + 1):
        sum += i * i
    return sum

# Функция для вычисления суммы квадратов с использованием reduce
def sum_of_squares_reduce(nsum):
    return reduce(lambda x, y: x + y * y, range(1, nsum + 1))

# Функция для измерения времени выполнения
def benchmark(func_name, number, nsum):
    if func_name == 'loop':
        func = lambda: sum_of_squares_loop(nsum)
    elif func_name == 'reduce':
        func = lambda: sum_of_squares_reduce(nsum)
    else:
        print("Не выбрана функция")
        return

    time = timeit.timeit(func, number=number)
    print(time)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Надо написать функцию, количество ее вызовов и число для суммы вычисления кадратов")
    else:
        func_name = sys.argv[1]
        number_of_calls = int(sys.argv[2])
        number_for_sum = int(sys.argv[3])
        benchmark(func_name, number_of_calls, number_for_sum)



# ./benchmark.py reduce 100000 5
# ./benchmark.py loop 8500000 11