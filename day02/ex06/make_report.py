import sys
from analytics import CoinFlipAnalyzer, Analytics
import config
import logging

def generate_report(file_path):
    analyzer = CoinFlipAnalyzer()
    data = analyzer.file_reader(file_path)

    calculations = CoinFlipAnalyzer.Calculations(data)
    heads_count, tails_count = calculations.counts()
    heads_fraction, tails_fraction = calculations.fractions(heads_count, tails_count)

    analytics = Analytics(data)
    predictions = analytics.predict_random(config.num_of_steps)
    predicted_heads = sum(row[0] for row in predictions)
    predicted_tails = sum(row[1] for row in predictions)

    total_observations = heads_count + tails_count
    report_text = config.report_template.format(
        total_observations=total_observations,
        tails_count=tails_count,
        heads_count=heads_count,
        tails_percentage=round(tails_fraction, 2),
        heads_percentage=round(heads_fraction, 2),
        num_of_steps=config.num_of_steps,
        predicted_tails=predicted_tails,
        predicted_heads=predicted_heads
    )

    analytics.save_file(report_text, 'report', 'txt')
    analytics.send_telegram_message("Отчет успешно создан")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Напиши, какой файл использовать")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        generate_report(file_path)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        analytics = Analytics([])
        analytics.send_telegram_message("Отчет не создан из-за ошибки")