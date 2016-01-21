def digit_to_roman(d, i):
    if i == 1000:
        return 'M' * d
    elif i == 100:
        if d < 4:
            return 'C' * d
        elif d == 4:
            return 'CD'
        elif d == 9:
            return 'CM'
        else:
            return 'D' + 'C' * (d - 5)
    elif i == 10:
        if d < 4:
            return 'X' * d
        elif d == 4:
            return 'XL'
        elif d == 9:
            return 'XC'
        else:
            return 'L' + 'X' * (d - 5)
    else:
        if d < 4:
            return 'I' * d
        elif d == 4:
            return 'IV'
        elif d == 9:
            return 'IX'
        else:
            return 'V' + 'I' * (d - 5)


def int2roman(num):
    if not isinstance(num, int) or num < 0 or num >= 4000:
        raise Exception('un-supported input')
    roman = ''
    for div in [1000, 100, 10, 1]:
        digit = num / div
        num = num % div
        roman += digit_to_roman(digit, div)
    return roman


def roman2int(roman):
    pair = [('I', 'V'), ('I', 'X'),
            ('X', 'L'), ('X', 'C'),
            ('C', 'D'), ('C', 'M')]
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for idx in range(len(roman) - 1):
        if (roman[idx], roman[idx + 1]) in pair:
            num -= value[roman[idx]]
        else:
            num += value[roman[idx]]
    num += value[roman[-1]]
    return num

