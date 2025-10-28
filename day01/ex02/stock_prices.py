import sys

def get_stock_price(company_name):
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

    if company_name in COMPANIES:
        stock_symbol = COMPANIES[company_name]
        if stock_symbol in STOCKS:
            print(STOCKS[stock_symbol])
        else:
            print("Unknown company")
    else:
        print("Unknown company")

def main():
    if len(sys.argv) == 2:
        company_name = sys.argv[1].capitalize()
        get_stock_price(company_name)

if __name__ == '__main__':
    main()