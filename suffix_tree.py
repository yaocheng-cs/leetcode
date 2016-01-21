class node(object):

    def __init__(self, val=None, edges={}):
        self.val = val
        self.edges = edges


class suffix_tree(object):

    def __init__(self, T):
        self.root = node()
        t = T + '$'
        # build the trie from every suffix of T
        for pos in range(len(t)):
            suffix = t[pos:]
            curr = self.root
            for c in suffix:
                try:
                    curr = curr.edges[c]
                except KeyError:
                    curr.edges[c] = node()
                    curr = curr.edges[c]
            curr.val = pos

        # turn the trie in to a campact tree, through depth first search
        stack = [(self.root, None, None)]  # (node, in_edge, parent)
        while stack:
            node, in_edge, parent = stack.pop()
            # no edge out - leaf node
            if not node.edges:
                continue
            # single edge out - current node should collapse with its only child
            elif len(node.edges.keys()) == 1:
                out_edge = node.edges.keys()[0]
                child = node.edges[out_edge]
                # point parent's combined edge to current node's only child
                parent[in_edge + out_edge] = child
                # push the new node into stack
                stack.append(child, in_edge + out_edge, parent)
                # delete current node (and parent's edge)
                del parent[in_edge]
            # multiple edges out - push all children into stack
            else:
                # reverse so the node is pop out in alphabetical order
                for edge in sorted(node.edges.keys(), reverse=True):
                    child = node[edge]
                    stack.append((child, edge, node))

        return self.root

    def ukkonen(self, T):
        return self.root

    def follow(self, S):
        pass

