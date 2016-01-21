class suffix_node(object):

    def __init__(self):
        self.out = {}
        self.back = None

    def follow_edge(self, char, grow=False):
        try:
            return self.out[char]
        except KeyError:
            if grow:
                self.out[char] = suffix_node()
                return self.out[char]
            else:
                raise

    def set_suffix_link(self, node):
        self.back = node

    def follow_suffix_link(self):
        return self.back


class suffix_tree(object):

    def __init__(self, S):
        self.root = suffix_node()
        pre = [self.root]
        for char in S + '$':
            curr = []
            for node in pre:
                curr.append(node.follow_edge(char, grow=True))
            curr.insert(0, self.root)
            for i in range(len(curr) - 1):
                curr[i + 1].set_suffix_link(curr[i])
            pre = curr

    def longest_common_substr(self, seq):
        longest = []
        max_len = 0
        temp = ''
        curr = self.root
        for char in seq:
            # after following suffix link from root, curr becomes none
            # we need to reset curr to root to resume the process
            if not curr:
                curr = self.root
            while True:
                try:
                    curr = curr.follow_edge(char)
                except KeyError:
                    curr = curr.follow_suffix_link()
                    if len(temp) > max_len:
                        longest = [temp]
                        max_len = len(temp)
                    elif len(temp) == max_len:
                        longest.append(temp)
                    temp = ''
                    # where there is no edge out from root for this char
                    # the char is not in the suffix tree alphabet. skip it
                    if not curr:
                        break
                else:
                    temp += char
                    break
        return longest


a = 'abccdbacdeef'
b = 'rabccdmacdeexcd'
tree = suffix_tree(a)
print tree.longest_common_substr(b)

