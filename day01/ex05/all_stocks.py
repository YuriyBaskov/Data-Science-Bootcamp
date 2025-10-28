import sys

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

def process_input(input_string):
    # Проверка на наличие двух запятых подряд
    if ',,' in input_string:
        return

    # Разделение строки на выражения
    expressions = [expr.strip() for expr in input_string.split(',')]

    # Проверка на наличие пустых выражений
    if any(expr == '' for expr in expressions):
        return

    for expr in expressions:
        # Нормализация регистра в нижний регистр
        normalized_expr = expr.lower()

        # Проверка, является ли выражение названием компании
        for company, ticker in COMPANIES.items():
            if company.lower() == normalized_expr:
                print(f"{company} stock price is {STOCKS[ticker]}")
                break
        else:
            # Проверка, является ли выражение тикером
            if normalized_expr in [ticker.lower() for ticker in STOCKS.keys()]:
                for ticker, price in STOCKS.items():
                    if ticker.lower() == normalized_expr:
                        print(f"{ticker} is a ticker symbol for {next(company for company, t in COMPANIES.items() if t == ticker)}")
                        break
            else:
                print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        process_input(sys.argv[1])