import sys


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  # a tree with no subtrees is still a bst


def is_bst(node, minim, maxim):
    # empty tree is bst
    if node is None:
        return 1
    # key outside range check
    if node.data < minim:
        return 0
    if node.data > maxim:
        return 0
    # update range sent to subtrees
    return is_bst(node.right, node.data, maxi) and is_bst(node.left, mini, node.data)


root = Tree(7)
root.left = Tree(4)
root.right = Tree(11)
root.left.left = Tree(3)
root.left.right = Tree(5)
root.right.left = Tree(10)
root.right.right = Tree(50)

mini = -sys.maxsize - 1
maxi = sys.maxsize
if is_bst(root, mini, maxi):
    print('is bst')
else:
    print('not a bst')
