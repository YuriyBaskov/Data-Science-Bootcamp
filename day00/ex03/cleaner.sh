#!/bin/sh

if [ ! -f "../ex02/hh_sorted.csv" ]; then
    echo "hh_sorted.csv не найден"
    exit 1
fi

echo "id,created_at,name,has_test,alternate_url" > hh_positions.csv

tail -n +2 ../ex02/hh_sorted.csv | while IFS=, read -r id created_at name has_test alternate_url; do
    # Ищем все грейды
    categories=$(echo "$name" | grep -Eo 'Junior|junior|Middle|middle|Senior|senior|Junior[/-]Middle|Junior[/-]middle|junior[/-]middle|Middle[/-]Senior|Middle[/-]senior|middle[/-]senior' | sort -u | tr '\n' '/' | sed 's/\/$//')
    # Если грейдов нет, пишем -
    if [ -z "$categories" ]; then
        categories="-"
    fi

    categories=$(echo "$categories" | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))} 1' OFS='/')
    
    echo "$id,$created_at,$categories,$has_test,$alternate_url" >> hh_positions.csv
done

echo "CSV файл создан: hh_positions.csv"