import json


with open('/Users/vasiliy/Downloads/food_services.json', encoding='utf-8') as file:
    shops = json.load(file)

districts_count = {}
shops_count = {}
for shop in shops:
    districts_count[shop['District']] = districts_count.get(shop['District'], 0) + 1
    shops_count[shop['OperatingCompany']] = shops_count.get(shop['OperatingCompany'], 0) + 1

del shops_count['']

print(*max(districts_count.items(), key=lambda x: x[1]), sep=': ')
print(*max(shops_count.items(), key=lambda x: x[1]), sep=': ')
