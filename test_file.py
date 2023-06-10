import sys
import pickle


name_func, *args = [arg.strip('\n') for arg in sys.stdin]

with open(name_func, 'rb') as pickle_file:
    pickle_func = pickle.load(pickle_file)

print(pickle_func(*args))
print(name_func)
print(args)
