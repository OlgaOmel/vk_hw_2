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

def dfs(left, right):
    if left == None or right == None:
        return 0
    
    count = 0 
    if left.val == right.val:
        count = 1
        
    count += dfs(left.left, right.right)
    count += dfs(left.right, right.left)
    return count

def count_mirror_twins(tree):
    if tree == None:
        return 0
    return dfs(tree.left, tree.right)


# Тест
def test_count_mirror_twins():
    test_tree_1 = build_tree([3, 9, 9, 6, 8, 8, 6], 0)
    test_tree_2 = build_tree([3, 9, 9, 6], 0)
    assert count_mirror_twins(test_tree_1) == 3
    assert count_mirror_twins(test_tree_2) == 1
    return True

test_count_mirror_twins()