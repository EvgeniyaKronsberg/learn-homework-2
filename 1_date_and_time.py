"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_today = date.today()
    delta_1 = timedelta(days=1)
    delta_30 = timedelta(days=30)
    dt_1_day = dt_today - delta_1
    dt_30_days = dt_today - delta_30

    print(f'Вчера: {dt_1_day}, Сегодня: {dt_today}, 30 дней назад: {dt_30_days}')
    


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    datetime_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return datetime_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
