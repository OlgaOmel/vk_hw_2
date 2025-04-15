def max_min_multplication(arr):
    if len(arr) < 3:
        return -1
    
    min_index = 1
    max_index = 2
    
    i = min_index
    while True:
        min_index_tmp = 2 * i + 1
        if min_index_tmp < len(arr):
            min_index = min_index_tmp
            i = min_index_tmp
            continue
        break
    
    i = max_index
    while True:
        max_index_tmp = 2 * i + 2
        if max_index_tmp < len(arr):
            max_index = max_index_tmp
            i = max_index_tmp
            continue
        break
              
    result = arr[min_index] * arr[max_index]
    return result


# Тест
def test_max_min_multiplication():
    test_arr = [16, 12, 18, 11, 15, 17, 21]
    assert max_min_multplication(test_arr) == 11*21
    return True

test_max_min_multiplication()