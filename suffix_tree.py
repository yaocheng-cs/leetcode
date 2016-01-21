class node(object):

    def __init__(self, val=None, edge={}):
        self.val = val
        self.edge = edge


class suffix_trie(object):

    def __init__(self, T):
        self.root = node()
        t = T + '$'
        for pos in range(len(t)):
            suffix = t[pos:]
            curr = self.root
            for c in suffix:
                try:
                    curr = curr.edge[c]
                except KeyError:
                    curr.edge[c] = node()
                    curr = curr.edge[c]
            curr.val = pos

        return self.root

    def ukkonen(self, T):
        return self.root

    def follow(self, S):
        pass

