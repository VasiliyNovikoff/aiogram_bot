from datetime import datetime


dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split(' ')]
days = []
for i in range(1, len(dates)):
    day = abs(dates[i] - dates[i - 1])
    days.append(day.days)
print(days)
