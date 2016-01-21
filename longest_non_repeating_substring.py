input_ = 'abcabcbb'

s = 0
e = 0
max_len = 0
results = []
nrs = {}

"""
while e < len(input_):
    e += 1
    char = input_[e - 1]
    try:
        nrs[char]
    except KeyError:
        nrs[char] = True
    else:
        if e - 1 - s > max_len:
            results = [(s, e - 1)]
            max_len = e - 1 - s
        elif e - 1 - s == max_len:
            results.append((s, e - 1))
        substr = input_[s: e - 1]
        idx = substr.index(char)
        for i in range(idx):
            del nrs[substr[i]]
        s += idx + 1
"""

while e < len(input_):
    char = input_[e]
    substr = input_[s: e]
    str_len = len(substr)
    idx = substr.find(char)
    if idx >= 0:
        if str_len > max_len:
            results = [(s, e)]
            max_len = str_len
        elif str_len == max_len:
            results.append((s, e))
        s += idx + 1
    e += 1

for r in results:
    print r, input_[r[0]: r[1]]

