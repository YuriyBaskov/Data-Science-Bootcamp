num_of_steps = 3

report_template = """Отчет

Мы сделали {total_observations} наблюдений при подбрасывании монеты: {tails_count} из них были решками и {heads_count} — орлами. Вероятности составляют {tails_percentage}% и {heads_percentage}% соответственно. Наш прогноз заключается в том, что в следующих {num_of_steps} наблюдениях у нас будет: {predicted_tails} решка и {predicted_heads} орла."""