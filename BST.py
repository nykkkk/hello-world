class BSTNode(object):  # 结点
    def __init__(self, t):
        self.key = t
        self.left = None
        self.right = None
        self.parent = None


class BST(object):  # 树
    def __init__(self, bls):
        self.root = BSTNode(bls[0])
        for bl in bls[1:]:
            self.insert(self.root, bl)

    def insert(self, root, t):
        if t < root.key:
            if root.left is None:
                root.left = BSTNode(t)
                root.left.parent = root
                return root.left
            else:
                return self.insert(root.left, t)
        else:
            if root.right is None:
                root.right = BSTNode(t)
                root.right.parent = root
                return root.right
            else:
                return self.insert(root.right, t)


def f_l(node, x):  # 找到次大结点
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node.key
    elif node.parent.parent.key > x:
        return node.parent.parent.key
    elif node.parent.left:
        return node.parent.key
    else:
        return None


def out1(node, x):  # 利用中序找到结点
    if node is not None:
        if (node.key == x):
            print(f_l(node, x))
        out1(node.left, x)
        out1(node.right, x)


def out(node):  # 中序遍历
    if node is not None:
        out(node.left)
        print(node.key)
        out(node.right)


def trimBST(node, minVal, maxval):  # 修剪
    if node is None:
        return
    node.left = trimBST(node.left, minVal, maxval)
    node.right = trimBST(node.right, minVal, maxval)
    if minVal <= node.key <= maxval:
        return node
    if node.key < minVal:
        return node.right
    if node.key > maxval:
        return node.left


bst = [3, 23, 5, 14, 67, 52, 99]
a = BST(bst)
print("次大结点为:")
out1(a.root, 52)
print("修剪后的树为:")
trim = trimBST(a.root, 5, 99)
out(trim)
