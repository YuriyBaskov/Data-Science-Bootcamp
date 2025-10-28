import sys
import time
import urllib3
from bs4 import BeautifulSoup

def get_financial_data(ticker, field):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker.lower()}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=headers)

    if response.status != 200:
        raise Exception(f"URL {url} не существует")

    soup = BeautifulSoup(response.data, 'html.parser')
    rows = soup.find_all('div', {'class': 'row lv-0 yf-t22klz'})

    field_data = []

    for row in rows:
        header = row.find('div', {'class': 'rowTitle yf-t22klz'})
        if header and header.text.strip() == field:
            cells = row.find_all('div', class_=lambda x: x and ('column yf-t22klz' in x or 'column yf-t22klz alt' in x))
            field_data = [cell.text.strip() for cell in cells if cell.text.strip()]
            break

    if not field_data:
        raise Exception(f"Поле '{field}' не найдено")

    return tuple([field] + field_data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Напиши тикер компании и что ищем")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        #time.sleep(5)  # Задержка в 5 секунд
        result = get_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print(f"Error: {e}")