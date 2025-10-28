#!/usr/bin/env python3

import timeit
import random
from collections import Counter

random_list = [random.randint(0, 100) for _ in range(1000000)]

# Функция для создания словаря из списка без Counter
def create_dict_without_counter(lst):
    result = {i: 0 for i in range(101)}
    for num in lst:
        result[num] += 1
    return result

# Функция для создания словаря из списка с Counter
def create_dict_with_counter(lst):
    return dict(Counter(lst))

# Функция для нахождения 10 самых распространенных чисел без Counter
# создаем словарь с количеством каждого числа, сортируем его по убыванию (True) количества и возвращаем 10 самых распространенных чисел
def top_10_without_counter(lst):
    count_dict = create_dict_without_counter(lst)
    return dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# Функция для нахождения 10 самых распространенных чисел с Counter
# тож самое, но возвращаем 10 самых распространенных чисел и помощью мост_комона
def top_10_with_counter(lst):
    count_dict = create_dict_with_counter(lst)
    return dict(Counter(count_dict).most_common(10))

def benchmark():
    # Измерение времени выполнения функций без Counter
    my_function_time = timeit.timeit(lambda: create_dict_without_counter(random_list), number=1)
    my_top_time = timeit.timeit(lambda: top_10_without_counter(random_list), number=1)

    # Измерение времени выполнения функций с Counter
    counter_function_time = timeit.timeit(lambda: create_dict_with_counter(random_list), number=1)
    counter_top_time = timeit.timeit(lambda: top_10_with_counter(random_list), number=1)

    print(f"my function: {my_function_time}")
    print(f"Counter: {counter_function_time}")
    print(f"my top: {my_top_time}")
    print(f"Counter's top: {counter_top_time}")

if __name__ == '__main__':
    benchmark()



# ./benchmark.py