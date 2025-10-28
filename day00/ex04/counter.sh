#!/bin/sh

if [ ! -f "../ex03/hh_positions.csv" ]; then
    echo "hh_positions.csv не найден"
    exit 1
fi

awk -F, '{print $3}' ../ex03/hh_positions.csv | tail -n +2 | sort | uniq -c | sort -nr > vrem_uniq.txt
# авк - извлекаем name, uniq - считаем уник строки, потом сорт по кол-ву в порядке убывания
echo "\"name\",\"count\"" > hh_uniq_positions.csv

# Чтение временного файла и форматирование данных для уник_позишнс
while IFS= read -r line; do
    count=$(echo "$line" | awk '{print $1}') #количество
    name=$(echo "$line" | awk '{print $2}') #имя
    echo "\"$name\",$count" >> hh_uniq_positions.csv
done < vrem_uniq.txt

# Удаление временного файла
rm vrem_uniq.txt

echo "CSV файл создан: hh_uniq_positions.csv"