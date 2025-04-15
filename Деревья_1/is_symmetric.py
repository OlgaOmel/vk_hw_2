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

        
def is_symmetric_bfs(tree):
    if tree == None:
        return True
    
    q = deque([tree])
    
    while len(q) > 0:
        q_len = len(q)
        for i in range(q_len):
            if q[i] == None and q[q_len - i - 1] == None:
                continue
            if q[i] == None or q[q_len - i - 1] == None:
                return False
            if q[i].val != q[q_len - i - 1].val:
                return False
            q.append(q[i].left)
            q.append(q[i].right)
        
        q = list(q)[q_len:]
    
    return True

# dfs  
def depth_search(tree, res):
    if tree == None:
        return res
    depth_search(tree.left, res)
    res.append(tree.val)
    depth_search(tree.right, res)
    return res

def is_symmetric_dfs(tree):
    if tree == None:
        return True
    val = []
    val = depth_search(tree, val)
    j = len(val) - 1
    for i in range(len(val) // 2):
        if val[i] != val[j]:
            return False
        j -= 1
    
    return True

# Тест
def test_is_symmetric_bfs():
    tree = build_tree([3, 8, 8, 9, 6, 6, 9], 0)
    assert is_symmetric_bfs(tree) == True
    return True

def test_is_symmetric_dfs():
    tree = build_tree([3, 8, 8, 9, 6, 6, 9], 0)
    assert is_symmetric_dfs(tree) == True
    return True

print(test_is_symmetric_bfs())
print(test_is_symmetric_dfs())
