def binary_search_sqrt(target):
    l = 0
    r = target
    
    while l <= r:
        middle = (l+r) // 2
        if middle * middle > target:
            r = middle - 1
        if middle * middle < target:
            l = middle + 1   
        return middle

# Тест
def test_binary_search_sqrt():
    test_target = 5
    assert binary_search_sqrt(test_target) == 2
    return True

test_binary_search_sqrt()
