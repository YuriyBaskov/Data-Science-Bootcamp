import sys
import time
import requests
from bs4 import BeautifulSoup
import pytest

def get_financial_data(ticker, field):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker.lower()}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"URL {url} does not exist")

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('div', {'class': 'row lv-0 yf-t22klz'})

    field_data = []

    for row in rows:
        header = row.find('div', {'class': 'rowTitle yf-t22klz'})
        if header and header.text.strip() == field:
            cells = row.find_all('div', class_=lambda x: x and ('column yf-t22klz' in x or 'column yf-t22klz alt' in x))
            field_data = [cell.text.strip() for cell in cells if cell.text.strip()]
            break

    if not field_data:
        raise Exception(f"Field '{field}' not found in the table")

    return tuple([field] + field_data)

# Тест для проверки, что функция возвращает корректные данные для действительного тикера и поля
def test_get_financial_data_valid_ticker():
    ticker = 'MSFT'
    field = 'Total Revenue'
    result = get_financial_data(ticker, field)
    assert isinstance(result, tuple)  # Проверка, что возвращаемый тип данных является кортежем
    assert result[0] == field
    assert all(isinstance(item, str) for item in result[1:])

# Тест для проверки, что функция вызывает исключение, если указан недействительный тикер
def test_get_financial_data_invalid_ticker():
    ticker = 'INVALIDTICKER'
    field = 'Total Revenue'
    with pytest.raises(Exception) as e:
        get_financial_data(ticker, field)
    assert "URL" in str(e.value) or "Field" in str(e.value)

# Тест для проверки, что функция вызывает исключение, если указано недействительное поле
def test_get_financial_data_invalid_field():
    ticker = 'MSFT'
    field = 'InvalidField'
    with pytest.raises(Exception) as e:
        get_financial_data(ticker, field)
    assert "Field" in str(e.value)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 financial_test.py <ticker> <field>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        time.sleep(5)  # Задержка в 5 секунд
        result = get_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    else:
        pytest.main([file])





#pytest financial_test.py 