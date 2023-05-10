from time import perf_counter, monotonic


def calculate_it(func, *args):
    start = perf_counter()
    result = func(*args)
    end = perf_counter() - start
    return end


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


my_iter = range(100_000)
print(calculate_it(for_and_append, my_iter))
print(calculate_it(list_comprehension, my_iter))
print(calculate_it(list_function, my_iter))
