import subprocess
import sys
import os
import shutil

def check_environment():
    # Проверяем, что скрипт запущен в виртуальной среде
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        raise EnvironmentError("Скрипт должен быть запущен в виртуальной среде")

def install_libraries():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке библиотек: {e}")

def list_installed_packages():
    try:
        # Отображаем все установленные библиотеки
        result = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        with open('requirements.txt', 'w') as f:
            f.write(result.decode('utf-8'))
        print("Библиотеки сохранены в requirements.txt")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при отображении установленных библиотек: {e}")

def archive_environment():
    try:
        # Архивируем виртуальную среду
        env_path = os.path.dirname(sys.executable)
        archive_name = 'env_archive.zip'
        shutil.make_archive(archive_name.replace('.zip', ''), 'zip', env_path)
        print(f"Виртуальная среда архивирована в {archive_name}")
    except Exception as e:
        print(f"Ошибка при архивировании виртуальной среды: {e}")

if __name__ == '__main__':
    try:
        check_environment()
        install_libraries()
        list_installed_packages()
        archive_environment()
    except EnvironmentError as e:
        print(f"Ошибка окружения: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")



#python3 librarian.py