import numpy as np
import matplotlib.pyplot as plt

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def draw(self):
        ## TODO: Fill this in.  You should definitely use recursion
        plt.axis("off")

def make_left_subtree():
    node = TreeNode(7)
    node.left = TreeNode(3)
    node.right = TreeNode(9)
    node.right.left = TreeNode(8)
    return node

def make_right_subtree():
    node = TreeNode(15)
    node.left = TreeNode(12)
    node.right = TreeNode(20)
    node.left.right = TreeNode(14)
    node.left.right.left = TreeNode(13)
    return node

def make_tree():
    T = BinaryTree()
    T.root = TreeNode(10)
    T.root.left = make_left_subtree()
    T.root.right = make_right_subtree()
    return T


T = make_tree()
T.draw()
plt.show()