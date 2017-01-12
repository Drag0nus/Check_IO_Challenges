def median(data):
    data = sorted(data)
    print(data)
    if len(data) % 2 != 0:
        return data[int(len(data)/2)]
    else:
        return float((data[int(len(data) / 2) - 1] +
                      data[int((len(data) / 2))]) / 2)


print(median([1, 2, 3, 4, 5]))
print(median([3, 2, 1, 4, 5]))
print(median([3, 2, 1, 4, 5, 6]))
print(median([1, 2, 3, 4, 5, 6]))
print(median([1, 300, 2, 200, 1]))
print(median(([3, 6, 20, 99, 10, 15])))
