# File: tree.py
# Follow your instructor closely
# to work out the tree ADT
from typing import Any
from collections import deque


class TreeNode:
    """ Stores one node of a general tree."""

    def __init__(self, val: Any):
        """ 
        Initialize the node with a value and no children.
        """
        self.val = val
        self.children = []

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)

    def add_children(self, new_children: list):
        """
        Adds the nodes in the children parameter
        to the list of children for the node.
        """
        self.children.extend(new_children)


class Tree:
    """ 
    Stores a general tree, where each node
    can have any number of children.
    """

    def __init__(self, root=None):
        """ 
        Initialize the root of the tree
        from the parameter root.
        """
        self.root = root

    def depth_first(self):
        """ 
        Performs depth-first traversal
        of the tree, printing out the value
        stored in each node.
        """
        # TODO provide your solution
        pass

    def size(self) -> int:
        """ return the number of nodes in the tree """

        # TODO provide your solution
        pass

    def num_leaf_nodes(self) -> int:
        """ return number of leaf nodes in the tree"""

        # TODO provide your solution
        pass

    def contains(self, val) -> bool:
        """ return true if the tree contains val else false"""

        # TODO provide your solution
        pass

    def breadth_first(self):
        """ preform a breadth-first traversal """

        # TODO provide your solution
        pass


if __name__ == "__main__":
    # Create a tree
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    h = TreeNode("h")
    i = TreeNode("i")
    j = TreeNode("j")
    k = TreeNode("k")
    l = TreeNode("l")
    m = TreeNode("m")
    j.add_children([k, l, m])
    h.add_children([j])
    e.add_children([h, i])
    c.add_children([e, f])
    d.add_children([g])
    a.add_children([b, c, d])
    tree = Tree(a)

    print("\nTesting depth-first traversal")
    print("Should print a b c e h j k l m i f d g")
    print("I'm printing", end=' ')
    tree.depth_first()

    print("\n\nTesting size")
    print("Should print 13")
    print("I'm printing", tree.size())

    print("\nTesting num_leaf_nodes")
    print("Should print 7")
    print("I'm printing", tree.num_leaf_nodes())

    print("\nTesting contains")
    print("Contains a?", tree.contains('a'))
    print("Contains g?", tree.contains('g'))
    print("Contains X?", tree.contains('x'))

    print("\nTesting breadth-first traversal")
    print("Should print a b c d e f g h i j k l m")
    print("I'm printing", end=' ')
    tree.breadth_first()
