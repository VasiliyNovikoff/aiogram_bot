# n - всего солдат
# каждый m-й солдат на убивание
def last(n, m):
    if n == 1:
        return n
    else:
        return 1 + (last(n - 1, m) + m - 1) % n


n = int(input())
m = int(input())
print(last(n, m))
