#1.
#Binary String Tree(BST) is a tree that all the leaves in the tree are string.
#2.
def total_len(BST):
    """takes a Binary String Tree and returns the sum of the lengths of all the leaves.

    BST -> num"""
    if isinstance(BST,tuple):
        return total_len(BST[0]) + total_len(BST[1])
    else:
        return len(BST)
#3.
def concat_leaves(BST):
    """takes a BST and returns a single string consisting of all the leaves concatenated together.

    BST -> str"""
    leaves = ""
    if isinstance(BST,tuple):
        return concat_leaves(BST[0]) + concat_leaves(BST[1])
    else:
        leaves = leaves + BST
        return leaves
#4.
def flatten(BST):
    """takes a BST and returns a single long tuple whose items are the leaves of the tree.

    BST -> str"""
    leaves = ()
    if isinstance(BST,tuple):
        return flatten(BST[0]) + flatten(BST[1])
    else:
        leaves = leaves + (BST,)
        return leaves
#5.
def initialize_tree(BST):
    """that takes a BST and returns a copy of that tree with all the leaves replaced by their first characters

    BST -> str"""
    if isinstance(BST,tuple):
        return (initialize_tree(BST[0]),initialize_tree(BST[1]))
    else:
        return BST[0]
#6.
def min_len(BST):
    """that takes a BST and returns a copy of that tree with all the leaves replaced by their first characters

    BST -> num"""
    if isinstance(BST,tuple):
        return min_len(BST[0]) + min_len(BST[1])
    else:
        return BST[0]









