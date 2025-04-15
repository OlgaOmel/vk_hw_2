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


def calculate_heights_and_balance(node):
    
    if not node:
        return 0
    
    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)

    node.balance_factor = left_height - right_height
    
    return 1 + max(left_height, right_height)
    

# Тест
def test_calculate_heights_and_balance():
    test_tree = build_tree([9, 3, 8, 16, 7, 11, 10], 0)
    assert calculate_heights_and_balance(test_tree) == 3
    return True

test_calculate_heights_and_balance()
