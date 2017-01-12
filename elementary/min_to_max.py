def min_element(args, **kwargs):
    key = kwargs.get('key', default=None)
    min_elem = args[0]
    if not key:
        for item in args:
            if item < min_elem:
                min_elem = itema
        return min_elem
    else:
        for item in args:
            if item < min_elem:
                min_elem = item
        return min_elem


def max_element(args):
    assert args
    max_elem = args[0]
    for item in args:
        if item > max_elem:
            max_elem = item
    return max_elem


print(min_element('hello'))
print(max_element('hello'))
print(max(2.2, 5.6, 5.9, key=int))
print(max(2.2, 5.6, 5.9))