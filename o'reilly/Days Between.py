from datetime import date


def days_diff(date1, date2):
    return abs(date(*date1) - date(*date2)).days


print(days_diff((1982, 4, 19), (1982, 4, 22)))
print(days_diff((2014, 1, 1), (2014, 8, 27)))
print(days_diff((2014, 8, 27), (2014, 1, 1)))
print(days_diff((2014, 1, 1), (2014, 8, 27)))
