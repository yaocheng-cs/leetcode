def break_ptn(ptn):
    parts = []
    for c in ptn:
        if c == '*':
            if len(parts) == 0 or len(parts[-1]) != 1:
                return None  #invalid pattern
            else:
                parts[-1].append(c)
        elif c == '.':
            parts.append([c])
        else:
            if (len(parts) > 0 and len(parts[-1]) == 2 and
                parts[-1][1] == '*' and parts[-1][0] == c):
                parts[-1].append(c)
            else:
                parts.append([c])
    return parts


def compare(c, p):
    """ 0: match, move forward cursor for both string and pattern
        -1: no match, move forward cursor for string
        1: no match, move forward cursor for pattern; pattern looks like 'a*', can match empty string
        2: no match, move forward cursor for pattern; pattern looks like 'a*a'; have to match at least one 'a'
        3: mismatch
    """
    if len(p) == 1:
        if p[0] == '.':
            return 0
        elif p[0] == c:
            return 0
        else:
            return 3
    elif len(p) == 2:
        if c == p[0] or p[0] == '.':  # '.*' can match 'ab'
            return -1
        #elif p[0] == '.':  # '.*' can match either 'aa' or 'bb', but not 'ab'
        #    p[0] = c
        #    return -1
        else:
            return 1
    elif len(p) == 3:
        if c == p[0]:
            return -1
        else:
            return 2


def is_match(s, ptn):
    parts = break_ptn(ptn)
    print parts
    if parts is None:
        print 'invalid pattern'
        return False

    s = iter(s)
    parts = iter(parts)
    c = p = '^'  # begin the comparison
    p_matched = False
    while True:
        res = compare(c, p)
        if res == 0:
            try:
                c = s.next()
            except StopIteration:
                try:
                    p = parts.next()
                except StopIteration:
                    return True
                else:
                    return False
            else:
                try:
                    p = parts.next()
                except StopIteration:
                    return False
                else:
                    p_matched = False
                    continue
        elif res == -1:
            try:
                c = s.next()
            except StopIteration:
                try:
                    p = parts.next()
                except StopIteration:
                    return True
                else:
                    return False
            else:
                p_matched = True
                continue
        elif res == 1:
            try:
                p = parts.next()
            except StopIteration:
                return False
            else:
                p_matched = False
                continue
        elif res == 2:
            if not p_matched:
                return False
            else:
                try:
                    p = parts.next()
                except StopIteration:
                    return False
                else:
                    p_matched = False
                    continue
        else:  # res == 3
            return False

