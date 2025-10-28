#!/usr/bin/env python3

import timeit

# Список адресов электронной почты
emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
          'anna@live.com', 'philipp@gmail.com']

# Дублируем циклом
def duplicate_with_loop(emails):
    result = []
    for email in emails:
        result.extend([email] * 5)
    return result

# Дублируем списочным включением
def duplicate_with_comprehension(emails):
    return [email for email in emails for _ in range(5)]

# Функция для измерения времени выполнения
def benchmark():
    loop_time = timeit.timeit(lambda: duplicate_with_loop(emails), number=9000000)
    comprehension_time = timeit.timeit(lambda: duplicate_with_comprehension(emails), number=9000000)

    if comprehension_time <= loop_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    print(f"{min(loop_time, comprehension_time)} vs {max(loop_time, comprehension_time)}")

if __name__ == '__main__':
    benchmark()



# ./benchmark.py