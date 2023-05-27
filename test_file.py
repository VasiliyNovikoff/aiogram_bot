import csv


with open('/Users/vasiliy/Downloads/prices.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))

cheap_list = []
for shop in reader:
    shop, *products = shop.items()
    cheap_list.append([shop, min(products, key=lambda stuff: (int(stuff[1]), stuff[0]))])

cheap_shop, cheap_product = min(cheap_list, key=lambda cheap: (int(cheap[1][1]), cheap[1][0], cheap[0][1]))
print(f'{cheap_product[0]}: {cheap_shop[1]}')
