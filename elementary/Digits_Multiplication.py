def digit_multi(number):
    result = 1
    for item in str(number):
        if item != str(0):
            result *= int(item)
    print(result)
    return result

digit_multi(000000)