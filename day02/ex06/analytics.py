import os
from random import randint
import logging
import requests

# Настройка логирования
logging.basicConfig(filename='analytics.log', level=logging.INFO, format='%(asctime)s %(message)s') 

class CoinFlipAnalyzer:
    def file_reader(self, file_path, has_header=True):
        logging.info("Чтение файла")
        data = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if has_header:
                header = lines[0].strip().split(',')
                if header[0].isdigit() and header[1].isdigit():
                    has_header = False # Нет заголовка
            if has_header:
                lines = lines[1:] # Пропуск заголовка, если он есть
            for line in lines:
                parts = line.strip().split(',') #удаляем пробелы и \n, разбиваем строку на части по запятой
                data.append([int(parts[0]), int(parts[1])])
        return data

    class Calculations:
        def __init__(self, data):
            logging.info("Инициализация Calculations")
            self.data = data

        def counts(self):
            logging.info("Подсчет количества орлов и решек")
            heads_count = sum(row[0] for row in self.data) # первый элемент каждой пары
            tails_count = sum(row[1] for row in self.data) # второй элемент каждой пары
            return heads_count, tails_count

        def fractions(self, heads_count, tails_count):
            logging.info("Вычисление долей орлов и решек")
            total = heads_count + tails_count
            heads_fraction = (heads_count / total) * 100
            tails_fraction = (tails_count / total) * 100
            return heads_fraction, tails_fraction

class Analytics(CoinFlipAnalyzer.Calculations):
    def predict_random(self, steps):
        logging.info("Прогнозирование случайных значений")
        predictions = []
        for _ in range(steps):
            heads = randint(0, 1)
            tails = 1 - heads
            predictions.append([heads, tails])
        return predictions

    def predict_last(self):
        logging.info("Прогнозирование последнего значения")
        return self.data[-1] if self.data else None

    def save_file(self, data, file_name, extension):
        logging.info("Сохранение файла")
        with open(f"{file_name}.{extension}", 'w') as file:
            file.write(data)

    def send_telegram_message(self, message):
        logging.info("Отправка сообщения в Telegram")
        telegram_url = "https://api.telegram.org/bot8118673999:AAGVEvy6DQFRfZ8ny9oQyy5ehxT3EpKib08/sendMessage"
        payload = {
            "chat_id": "-1002361796585",
            "text": message
        }
        response = requests.post(telegram_url, json=payload)
        return response