def abs_sorting(numbers_array):
    return sorted(numbers_array, key=lambda x: abs(x))


print(abs_sorting((-20, -5, 10, 15)))
print(abs_sorting((1, 2, 3, 0)))
print(abs_sorting((-1, -2, -3, 0)))