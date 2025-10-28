#!/bin/sh

if [ ! -f "../ex03/hh_positions.csv" ]; then
    echo "hh_positions.csv не найден"
    exit 1
fi

tail -n +2 ../ex03/hh_positions.csv | while IFS=, read -r id created_at name has_test alternate_url; do
    date=$(echo "$created_at" | cut -d'T' -f1) # Извлечение даты
    filename="hh_positions_$date.csv"

    echo "$id,$created_at,$name,$has_test,$alternate_url" >> "$filename"   
done

echo "Файлы созданы по датам"