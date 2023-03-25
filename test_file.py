def chunked(s, n):
    li: list = []
    for i in range(len(s)):
        if not li:
            li.append([s[i]])
        elif i % n != 0:
            li[-1].extend([s[i]])
        else:
            li.append([s[i]])
    return li


s = input().split()
n = int(input())

print(chunked(s, n))
