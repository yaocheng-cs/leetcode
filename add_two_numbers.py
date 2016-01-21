class Digit(object):

    def __init__(self, val, nxt=None):
        if val not in range(10):
            raise ValueError(val)
        self.value = val
        self.next_ = nxt


class LinkNum(object):

    def __init__(self, val):
        if val < 0:
            raise ValueError(val)
        elif val == 0:
            self.value = 0
            self.lowest_digit = Digit(0)
        else:
            self.value = val
            pre_digit = None
            while val > 0:
                cur_digit = Digit(val % 10)
                if pre_digit:
                    pre_digit.next_ = cur_digit
                else:
                    self.lowest_digit = cur_digit
                val = val / 10
                pre_digit = cur_digit

    def get_value(self):
        value = 0
        weight = 1
        cur_digit = self.lowest_digit
        while cur_digit:
            value += cur_digit.value * weight
            cur_digit = cur_digit.next_
            weight *= 10
        return value

    def __str__(self):
        buf = ''
        cur_digit = self.lowest_digit
        while cur_digit:
            buf += str(cur_digit.value)
            buf += ' --> '
            cur_digit = cur_digit.next_
        return buf[:-5]


def digit_plus(d1, d2):
    promote = 0
    pre_digit = None
    while (d1 or d2 or promote):
        temp = []
        if d1:
            temp.append(d1.value)
            d1 = d1.next_
        if d2:
            temp.append(d2.value)
            d2 = d2.next_
        if promote:
            temp.append(promote)
        sum_ = sum(temp)
        cur_digit = Digit(sum_ % 10)
        if pre_digit:
            pre_digit.next_ = cur_digit
        else:
            lowest_digit = cur_digit
        pre_digit = cur_digit
        promote = sum_ / 10
    return lowest_digit


def print_digit(digit):
    buf = ''
    cur_digit = digit
    while cur_digit:
        buf += str(cur_digit.value)
        buf += ' --> '
        cur_digit = cur_digit.next_
    print buf[:-5]


num1 = LinkNum(1092)
num2 = LinkNum(293)
print num1
print num2
sum_ = num1.get_value() + num2.get_value()
print LinkNum(sum_)
sum_ = digit_plus(num1.lowest_digit, num2.lowest_digit)
print_digit(sum_)

