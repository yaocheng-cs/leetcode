import math

def reverse(n):
    if n == 0:
        return n
    neg = False
    if n < 0:
        neg = True
        n = 0 - n
    digits = []
    while n > 0:
        mod = n % 10
        digits.append(mod)
        n = n / 10
    print digits
    rev = 0
    length = len(digits)
    for i in range(length):
        rev += digits[i] * math.pow(10, length - 1 - i)
    if neg:
        return int(0 - rev)
    else:
        return int(rev)


print reverse(1234)
print reverse(0)
print reverse(-98167)
