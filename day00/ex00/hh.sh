#!/bin/sh

vacancy_name="$1"

if [ -z "$vacancy_name" ]; then
    echo "Usage: $0 "
    exit 1
fi

cvacancy_name=$(printf %s "$vacancy_name" | jq -sRr @uri)

api_url="https://api.hh.ru/vacancies?text=$cvacancy_name&search_field=name&per_page=20"

curl -s "$api_url" | jq '.' > hh.json

if [ ! -s hh.json ]; then
    echo "Не удалось получить данные"
    exit 1
fi

echo "Данные успешно сохранены в файле hh.json"
exit 0