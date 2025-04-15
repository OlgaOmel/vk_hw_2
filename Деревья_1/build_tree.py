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
        

# Тест
def test_build_tree():
    test_arr = [8, 9, 11, 7, 16, 3, 1]
    tree = build_tree(test_arr, 0)
    assert tree.val == 8
    assert tree.left.val == 9
    assert tree.right.val == 11
    assert tree.left.left.val == 7
    assert tree.left.right.val == 16
    assert tree.right.left.val == 3
    assert tree.right.right.val == 1
    return True

test_build_tree()