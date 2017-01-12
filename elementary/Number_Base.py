
def check_io(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1


check_io("AF", 16) == 175, "Hex"
check_io("101", 2) == 5, "Bin"
check_io("101", 5) == 26, "5 base"
check_io("Z", 36) == 35, "Z base"
check_io("AB", 10) == -1, "B > A > 10"
