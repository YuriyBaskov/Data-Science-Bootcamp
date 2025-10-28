#!/bin/sh

if [ -z "$(ls hh_positions_*.csv 2>/dev/null)" ]; then
    echo "Файлы hh_positions_*.csv не найдены"
    exit 1
fi

echo "id,created_at,name,has_test,alternate_url" > hh_positions_combined.csv

# Объединение всех файлов в один
for file in hh_positions_*.csv; do
    cat "$file" >> hh_positions_combined.csv
done

echo "Файлы объединены в hh_positions_combined.csv"