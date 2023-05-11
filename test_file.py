from datetime import date
import calendar


def get_all_thursday(year):
    date_list = []
    for month in range(1, 13):
        month_cal = calendar.monthcalendar(year, month)
        first_thursday = month_cal[0][3]
        third_thursday = month_cal[2][3] if first_thursday != 0 else month_cal[3][3]
        date_list.append(date(year, month, third_thursday))
    return print_date(date_list)


def print_date(date_list: list[date]):
    for dt in date_list:
        print(dt.strftime('%d.%m.%Y'))


get_all_thursday(int(input()))
