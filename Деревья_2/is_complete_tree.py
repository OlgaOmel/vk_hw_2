from collections import deque

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

def is_complete_tree(tree):
    if not tree:
        return True 
    
    q = deque([tree])
    should_be_leaf = False
    
    while len(q) > 0:
        node = q.popleft()

        if not node:
            should_be_leaf = True
        else:
            if should_be_leaf:
                return False
            q.append(node.left)
            q.append(node.right)
            
    return True


# Тест
def test_is_complete_tree():
    test_tree = build_tree([8, 3, 9, 11, 6], 0)
    assert is_complete_tree(test_tree) == True
    return True

test_is_complete_tree()