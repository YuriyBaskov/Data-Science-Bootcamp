import sys

def get_stock_price(ticker_symbol):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

# Создаем обратный словарь для поиска компании по тикеру
    REVERSE_COMPANIES = {v: k for k, v in COMPANIES.items()}

    if ticker_symbol.upper() in STOCKS:
        company_name = REVERSE_COMPANIES.get(ticker_symbol.upper(), "Unknown company")
        stock_price = STOCKS[ticker_symbol.upper()]
        print(f"{company_name} {stock_price}")
    else:
        print("Unknown ticker")

def main():
    if len(sys.argv) == 2:
        company_name = sys.argv[1].capitalize()
        get_stock_price(company_name)

if __name__ == '__main__':
    main()