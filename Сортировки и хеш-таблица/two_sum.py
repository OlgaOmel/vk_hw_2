def two_sum(arr, target):
    cache = {}

    for index, value in enumerate(arr):
        cache[value] = index
        diff = target - value
        if diff in cache:
            return [cache[diff], index]         
    return []

# Тест
def test_two_sum():
    test_arr = [1,2,3]
    test_target = 3
    assert two_sum(test_arr, test_target) == [0,1]
    return True

test_two_sum()