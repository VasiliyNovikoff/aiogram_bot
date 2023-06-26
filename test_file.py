import string

alphabet = string.ascii_lowercase

new_alphabet = input()
string = input().lower()

tbl = string.maketrans(alphabet, new_alphabet)
print(string.translate(tbl))
