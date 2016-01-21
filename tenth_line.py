fp = open('input.txt', 'r')
try:
    print fp.readlines()[9]
except IndexError:
    print 'input.txt contains less than 10 lines'

