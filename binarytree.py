# File: binarytree.py
# Follow your instructor closely

from collections import deque


class BinaryTreeNode:

    def __init__(self, val, left=None, right=None):
        """ 
        Initialize the node with a value,
        with left child from the parameter left 
        and the right child from the parameter right.
        """
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)


class BinaryTree:

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
        self._depth_first_recur(self.root)

    def _depth_first_recur(self, cur):
        """ perform a depth-first traversal of the tree
        rooted at cur """
        if cur is None:
            return
        print(cur, end=' ')
        self._depth_first_recur(cur.left)
        self._depth_first_recur(cur.right)

    def size(self) -> int:
        """ return the number of nodes in the tree """
        return self._size_recur(self.root)

    def _size_recur(self, cur: BinaryTreeNode) -> int:
        """ return number of nodes in the subtree rooted at node """
        if cur is None:
            return 0
        return 1 + self._size_recur(cur.left) + self._size_recur(cur.right)

    def num_leaf_nodes(self) -> int:
        """ return number of leaf nodes in the tree"""
        return self._num_leaf_nodes_recur(self.root)

    def _num_leaf_nodes_recur(self, node) -> int:
        """ return number of leaf nodes of the subtree rooted at node"""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1

        cur_count = 0
        left_count = self._num_leaf_nodes_recur(node.left)
        right_count = self._num_leaf_nodes_recur(node.right)

        return cur_count + left_count + right_count

    def contains(self, val) -> bool:
        """ return true if the tree contains val else false"""
        return self._contains_recur(self.root, val)

    def _contains_recur(self, node, val) -> bool:
        """ check if the subtree rooted at node contains <val> or not"""
        if node is None:
            return False

        if node.val == val:
            return True

        left_check = self._contains_recur(node.left, val)
        right_check = self._contains_recur(node.right, val)

        return left_check or right_check


if __name__ == "__main__":
    # Create tree nodes
    zi = BinaryTreeNode('ziggy')
    sh = BinaryTreeNode('sheila', zi)
    si = BinaryTreeNode('simon')
    ma = BinaryTreeNode('matrha')
    mi = BinaryTreeNode('milton')
    le = BinaryTreeNode('leon', sh, si)
    an = BinaryTreeNode('andrea', ma, mi)
    ca = BinaryTreeNode('carey', le, an)

    # Create tree
    tree = BinaryTree(ca)

    print("Testing depth-first traversal")
    print("Should print carey leon sheila ziggy simon andrea matrha milton")
    print("I'm printing", end=' ')
    tree.depth_first()

    print("\n\nTesting size")
    print("Should print 8")
    print("I'm printing", tree.size())

    print("\nTesting num_leaf_nodes")
    print("Should print 4")
    print("I'm printing", tree.num_leaf_nodes())

    print("\nTesting contain")
    print("Contains Sheila?", tree.contains('sheila'))
    print("Contains Leon?", tree.contains('leon'))
    print("Contains David?", tree.contains('david'))
