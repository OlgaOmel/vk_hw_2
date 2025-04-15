from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0


def build_tree(arr, i):
    if i >= len(arr):
        return None
    
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    
    return root


def mirror_tree(tree):
    
    if tree == None:
        return None
    
    tree.left, tree.right = tree.right, tree.left 

    mirror_tree(tree.left)
    mirror_tree(tree.right)
    
    return tree

def mirror_tree_iterative(tree):
    if tree == None:
        return None
    
    q = deque([tree])
    
    while len(q) > 0:
        current = q.popleft()
        
        temp = current.left
        current.left = current.right
        current.right = temp
        
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return tree


# Тест
def test_mirror_tree():
    test_tree = build_tree([1, 2, 3, 4, 5, 6, 7], 0)
    assert test_tree.left.left.val == 4
    mirror_tree(test_tree)
    assert test_tree.left.left.val == 7
    return True

def test_mirror_tree_iterative():
    test_tree = build_tree([1, 2, 3, 4, 5, 6, 7], 0)
    assert test_tree.left.left.val == 4
    mirror_tree_iterative(test_tree)
    assert test_tree.left.left.val == 7
    return True

print(test_mirror_tree())
print(test_mirror_tree_iterative())
