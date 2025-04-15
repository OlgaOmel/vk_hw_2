class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr, i):
    if i >= len(arr):
        return None
    
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    
    return root

def is_same_tree(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right) 

def is_subtree(a, b):
    if b == None:
        return True
    if a == None:
        return False
    if is_same_tree(a, b):
        return True
    return is_subtree(a.left, b) or is_subtree(a.right, b) 


# Тест
def test_is_subtree():
    test_tree_1 = build_tree([3, 8, 8, 9, 6], 0)
    test_tree_2 = build_tree([8, 9, 6], 0)
    test_tree_3 = build_tree([5, 3, 2], 0)
    assert is_subtree(test_tree_1, test_tree_2) == True
    assert is_subtree(test_tree_1, test_tree_3) == False
    return True

test_is_subtree()