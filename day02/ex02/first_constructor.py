import sys

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            
            if len(lines) < 2:
                raise ValueError("Напиши заголовок и хотя бы одну строку данных")

            header = lines[0].strip().split(',')
            if len(header) != 2:
                raise ValueError("В заголовке должно быть две строки через запятую")
            
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) != 2 or not (parts[0] in ['0', '1'] and parts[1] in ['0', '1']):
                    raise ValueError("Каждая строка данных должна содержать 0 или 1 через запятую")
                if parts[0] == parts[1]:
                    raise ValueError("Значения повторяются в какой-то строке, надо исправить")
            return ''.join(lines)
        except Exception as e:
            raise ValueError(f"Ошибка чтения файла {e}")
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Напиши, какой файл использовать")
        sys.exit(1)

    file_path = sys.argv[1]
    research = Research(file_path)

    try:
        content = research.file_reader()
        print(content)
    except ValueError as e:
        print(e)