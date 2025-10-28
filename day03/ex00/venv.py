#!/usr/bin/env python3

import os

def print_virtual_env():
    try:
        virtual_env = os.environ['VIRTUAL_ENV'] # получить значение переменной окружения VIRTUAL_ENV
        print(f"Текущая виртуальная среда {virtual_env}")
    except KeyError:
        print(f"Не активирована витруальная среда")

if __name__ == '__main__':
    print_virtual_env()




#python3 -m venv charmaip
#source charmaip/bin/activate
#deactivate