import csv


with open('/Users/vasiliy/Downloads/titanic.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))

reader.sort(key=lambda item: item['sex'], reverse=True)
for passenger in reader:
    if int(passenger['survived']) and float(passenger['age']) < 18:
        print(passenger['name'])
