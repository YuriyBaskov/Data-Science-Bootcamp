#!/bin/sh

if [ ! -f "../ex01/hh.csv" ]; then
    echo "hh.csv не найден"
    exit 1
fi

echo "id,created_at,name,has_test,alternate_url" > hh_sorted.csv

tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1 | cat >> hh_sorted.csv

echo "CSV файл отсортирован: hh_sorted.csv"