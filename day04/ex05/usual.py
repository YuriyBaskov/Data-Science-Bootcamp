#!/usr/bin/env python3
# Этот скрипт читает все строки файла в список и измеряет пиковое использование памяти и время выполнения

import sys
import time
import resource

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def main():
    if len(sys.argv) != 2:
        print("Напиши скрипт и какой файл открыть")
        return

    file_path = sys.argv[1]

    start_time = time.time()
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # 

    lines = read_file(file_path)
    for line in lines:
        pass

    end_time = time.time()
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    peak_memory_usage = (end_memory - start_memory) / (1024 * 1024)  # Конвертируем в гб
    total_time = end_time - start_time

    print(f"Peak Memory Usage = {peak_memory_usage:.3f} GB") # Пиковое использование памяти
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s") # Время пользовательского режима + время системного режима

if __name__ == '__main__':
    main()





# ./usual.py ratings.csv