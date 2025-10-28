def process_countries():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    # Преобразуем список кортежей в словарь
    country_dict = dict(list_of_tuples)

    # Сортируем словарь по значениям в порядке убывания, а затем по ключам в алфавитном порядке
    sorted_countries = sorted(country_dict.items(), key=lambda item: (-int(item[1]), item[0]))

    # Выводим названия стран
    for country, _ in sorted_countries:
        print(country)

if __name__ == '__main__':
    process_countries()