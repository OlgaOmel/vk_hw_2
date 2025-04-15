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

def in_order_min_iterative(node, k):
    
    stack = []
    counter = 0
    current = node
    
    while len(stack) > 0 or current != None:
        while current != None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        
        if counter == k:
            return current.val
        current = current.right
    return None

def in_order_min(node, k, counter):
    
    if node == None:
        return None
    
    left_result = in_order_min(node.left, k, counter)
    if left_result != None:
        return left_result
    
    counter[0] += 1
    if counter[0] == k:
        return node.val
    
    return in_order_min(node.right, k, counter)
    

# Тест
def test_in_order_min_iterative():
    test_tree = build_tree([16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27], 0)
    assert in_order_min_iterative(test_tree, 2) == 6
    return True

def test_in_order_min():
    test_tree = build_tree([16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27], 0)
    assert in_order_min(test_tree, 1, [0]) == 2
    return True

print(test_in_order_min_iterative())
print(test_in_order_min())
