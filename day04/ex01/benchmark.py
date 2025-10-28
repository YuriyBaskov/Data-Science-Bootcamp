#!/usr/bin/env python3

import timeit

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

# Функция для измерения времени выполнения
def benchmark():
    loop_time = timeit.timeit(lambda: duplicate_with_loop(emails), number=9000000)
    comprehension_time = timeit.timeit(lambda: duplicate_with_comprehension(emails), number=9000000)
    map_time = timeit.timeit(lambda: duplicate_with_map(emails), number=9000000)

    times = [loop_time, comprehension_time, map_time]
    sorted_times = sorted(times)

    if sorted_times[0] == map_time:
        print("it is better to use a map")
    elif sorted_times[0] == comprehension_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    print(f"{sorted_times[0]} vs {sorted_times[1]} vs {sorted_times[2]}")

if __name__ == '__main__':
    benchmark()



# ./benchmark.py