from datetime import date, timedelta


def saturdays_between_two_dates(start, end):
    saturday_count = 0
    if end < start:
        start, end = end, start
    while start <= end:
        if start.isoweekday() == 6:
            saturday_count += 1
            start += timedelta(7)
            continue
        start += timedelta(1)
    return saturday_count


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
