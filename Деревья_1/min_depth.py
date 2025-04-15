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

def min_depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    if tree.left != None and tree.right != None:
        return 1 + min(min_depth(tree.left), min_depth(tree.right))
    if tree.left != None:
        return 1 + min_depth(tree.left)
    if tree.right != None:
        return 1 + min_depth(tree.right)
    
    
# Тест
def test_min_depth():
    test_tree = build_tree([3, 8, 8, 9, 6], 0)
    assert min_depth(test_tree) == 2
    return True

test_min_depth()
