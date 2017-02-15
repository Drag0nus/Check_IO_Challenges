# generates list of first 20 fibonacci numbers to compare with
def fibonacci():
    result = [0, 1]
    while len(result) < 20:
        result.append(result[len(result) - 1] + result[len(result) - 2])
    return result


# generates dictionary of dependencies between opacity and age of ghost
def ghosts_age():
    age_dict = {}
    max_opacity = 10000
    age = 0

    for i in range(0, 5000):
        if age in fibonacci():
            max_opacity -= age
        else:
            max_opacity += 1

        age_dict[age] = max_opacity
        age += 1
    return age_dict


def check_io(opacity):
    for key in ghosts_age():
        if ghosts_age()[key] == opacity:
            return key


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert check_io(10000) == 0, "Newborn"
    assert check_io(9999) == 1, "1 year"
    assert check_io(9997) == 2, "2 years"
    assert check_io(9994) == 3, "3 years"
    assert check_io(9995) == 4, "4 years"
    assert check_io(9990) == 5, "5 years"
