from datetime import datetime


n = int(input())
employments = [input() for _ in range(n)]
pattern = '%d.%m.%Y'
employments_dict: dict = {}

for employment in employments:
    date_key = datetime.strptime(employment.split(' ')[-1], pattern)
    date_value = employment.split(' ')[0] + ' ' + employment.split(' ')[1]
    employments_dict[date_key] = employments_dict.get(date_key, 0) + 1

new_employments_list = sorted(employments_dict.items(), key=lambda k: (-k[1], k[0]))

for i in range(len(new_employments_list)):
    if new_employments_list[i][1] == new_employments_list[0][1]:
        print(new_employments_list[i][0].strftime(pattern))
    else:
        break
