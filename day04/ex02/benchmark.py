#!/usr/bin/env python3

import timeit
import sys

# Список адресов электронной почты
emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
          'anna@live.com', 'philipp@gmail.com']

# Дублируем циклом
# для каждого адреса в списке emails добавляем его пять раз в result с помощью extend
def duplicate_with_loop(emails):
    result = []
    for email in emails:
        result.extend([email] * 5)
    return result

# Дублируем списочным включением
# для каждого адреса в списке emails мы создаем пять копий этого адреса
def duplicate_with_comprehension(emails):
    return [email for email in emails for _ in range(5)]


# Дублируем картой
# Лямбда создает список, содержащий пять копий каждого адреса, результат map преобразуется в список с помощью list
def duplicate_with_map(emails):
    return list(map(lambda email: [email] *5, emails))

# Дублируем фильтром
# применяет лямбду к каждому элементу списка emails и возвращает только те элементы, для которых функция возвращает True
def duplicate_with_filter(emails):
    return list(filter(lambda email: email.endswith('@gmail.com'), emails))

# Функция для измерения времени выполнения
def benchmark(func_name, number):
    if func_name == 'loop':
        func = lambda: duplicate_with_loop(emails)
    elif func_name == 'list_comprehension':
        func = lambda: duplicate_with_comprehension(emails)
    elif func_name == 'map':
        func = lambda: duplicate_with_map(emails)
    elif func_name == 'filter':
        func = lambda: duplicate_with_filter(emails)
    else:
        print("Не выбрана функция")
        return

    time = timeit.timeit(func, number=number)
    print(time)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Надо написать функцию и количество ее вызовов")
    else:
        func_name = sys.argv[1]
        number_of_calls = int(sys.argv[2])
        benchmark(func_name, number_of_calls)



# ./benchmark.py map 1000000
# ./benchmark.py filter 1000000
# ./benchmark.py loop 1000000
# ./benchmark.py list_comprehension 1000000