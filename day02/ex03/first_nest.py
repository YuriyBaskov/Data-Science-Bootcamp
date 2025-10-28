import sys

class CoinFlipAnalyzer:
    def file_reader(self, file_path, has_header=True):
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
        # Статические методы не привязаны к экземпляру класса и не имеют доступа к атрибутам экземпляра или класса.
        @staticmethod
        def counts(data):
            heads_count = sum(row[0] for row in data) # первый элемент каждой пары
            tails_count = sum(row[1] for row in data) # второй элемент каждой пары
            return heads_count, tails_count

        @staticmethod
        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            heads_fraction = (heads_count / total) * 100
            tails_fraction = (tails_count / total) * 100
            return heads_fraction, tails_fraction

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Напиши, какой файл использовать")
        sys.exit(1)

    file_path = sys.argv[1]
    analyzer = CoinFlipAnalyzer()
    data = analyzer.file_reader(file_path)
    print(data)

    heads_count, tails_count = CoinFlipAnalyzer.Calculations.counts(data)
    print(f"{heads_count} {tails_count}")

    heads_fraction, tails_fraction = CoinFlipAnalyzer.Calculations.fractions(heads_count, tails_count)
    print(f"{heads_fraction} {tails_fraction}")