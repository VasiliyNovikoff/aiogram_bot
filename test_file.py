import sys


socks_counts = list(map(str.strip, sys.stdin))
players = ['Дима', 'Анри']
print(players[(len(socks_counts) + int(socks_counts[-1])) % 2])
