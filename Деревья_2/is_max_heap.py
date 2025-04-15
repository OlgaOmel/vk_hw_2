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

def is_max_heap_1(arr):
    n = len(arr)
    for i in range(n-1):
        left = 2 * i - 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def is_max_heap_2(tree):
    if not tree:
        return True 

    q = deque([tree])
    should_be_leaf = False

    while len(q) > 0:
        current = q.popleft()

        if current.left:
            if should_be_leaf or current.left.val > current.val:
                return False
            q.append(current.left)
        else:
            should_be_leaf = True  

        if current.right:
            if should_be_leaf or current.right.val > current.val:
                return False
            q.append(current.right)
        else:
            should_be_leaf = True

    return True

# Тест
def test_is_max_heap_1():
    test_arr_1 = [3, 8, 8, 9, 6]
    test_arr_2 = [10, 9, 8, 7, 6, 5, 4]
    assert is_max_heap_1(test_arr_1) == False
    assert is_max_heap_1(test_arr_2) == True

    return True

test_is_max_heap_1()


def test_is_max_heap_2():
    test_tree_1 = build_tree([3, 8, 8, 9, 6], 0)
    test_tree_2 = build_tree([10, 9, 8, 7, 6, 5, 4], 0)
    assert is_max_heap_2(test_tree_1) == False
    assert is_max_heap_2(test_tree_2) == True

    return True

print(test_is_max_heap_1())
print(test_is_max_heap_2())




