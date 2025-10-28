def read_and_write():
    try:
        with open('ds.csv', 'r', encoding='utf-8') as csv_file:
            lines = csv_file.readlines()

        with open('ds.tsv', 'w', encoding='utf-8') as tsv_file:
            for line in lines:
                # Создаем пустой список для хранения полей
                fields = []
                # Создаем временную строку для накопления символов
                temp_field = ''
                # Флаг для отслеживания, находимся ли мы внутри кавычек
                in_quotes = False

                for char in line:
                    if char == '"':
                        # Переключаем флаг, если встречаем кавычку
                        in_quotes = not in_quotes
                    elif char == ',' and not in_quotes:
                        # Если встречаем запятую вне кавычек, добавляем поле в список
                        fields.append(temp_field.strip())
                        temp_field = ''
                    else:
                        # Добавляем символ к временной строке
                        temp_field += char

                # Добавляем последнее поле
                fields.append(temp_field.strip())

                # Объединяем поля с помощью таб и записываем в файл
                tsv_line = '\t'.join(fields)
                tsv_file.write(tsv_line + '\n')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    read_and_write()