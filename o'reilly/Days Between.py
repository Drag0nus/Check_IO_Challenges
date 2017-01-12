from datetime import date


def days_diff(date1, date2):
    first_date = date(*date1)
    second_date = date(*date2)
    return abs(first_date - second_date).days


print(days_diff((1982, 4, 19), (1982, 4, 22)))
print(days_diff((2014, 1, 1), (2014, 8, 27)))
print(days_diff((2014, 8, 27), (2014, 1, 1)))
print(days_diff((2014, 1, 1), (2014, 8, 27)))
