#!/bin/sh

if [ ! -f "../ex00/hh.json" ]; then
    echo "hh.json не найден"
    exit 1
fi
if [ ! -f "filter.jq" ]; then
    echo "filter.jq не найден"
    exit 1
fi

echo "id,created_at,name,has_test,alternate_url" > hh.csv

jq -r -f filter.jq ../ex00/hh.json >> hh.csv

echo "CSV файл сгенерирован: hh.csv"