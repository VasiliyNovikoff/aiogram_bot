import csv
from datetime import datetime


with open('/Users/vasiliy/Downloads/name_log.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file))

pattern = '%d/%m/%Y %H:%M'
reader.sort(key=lambda item: (item['email'], -datetime.strptime(item['dtime'], pattern).timestamp()))

new_reader = []
email_list = []
for user in reader:
    if user['email'] not in email_list:
        new_reader.append(user)
        email_list.append(user['email'])

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader[0].keys())
    writer.writeheader()
    writer.writerows(new_reader)
