import math

def num_of_digit(n):
    num = 0
    n = abs(n)
    while n > 0:
        num += 1
        n = n / 10
    return num

def is_palindrome(n):
    digit = num_of_digit(n)
    if digit == 1:
        return True
    left = digit - 1
    right = 1
    res1 = res2 = abs(n)
    while left >= right:
        test1 = res1 / int(math.pow(10, left))
        test2 = res2 % 10
        if test1 != test2:
            return False
        else:
            res1 = res1 % int(math.pow(10, left))
            res2 = res2 / 10
            left -= 1
            right += 1
    return True

for n in [12321, -151, -9, 11011, -22, -243, 0]:
    print n, is_palindrome(n)

