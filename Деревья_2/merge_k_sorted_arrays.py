import heapq


def merge_k_sorted_arrays_1(arrs):
    
    min_heap = []
    
    for i in range(len(arrs)):
        for j in range(len(arrs[i])):
            heapq.heappush(min_heap, arrs[i][j])
    
    merged_array = []
    while len(min_heap) > 0:
        merged_array.append(heapq.heappop(min_heap))
    return merged_array
            

def merge_k_sorted_arrays_2(arrs):
   
    merged_array = []
    min_heap = []
    
    for i in range(len(arrs)):
        current_array = arrs[i]
        if len(current_array) > 0:
            heapq.heappush(min_heap, [current_array[0], i, 0])
    
    
    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        
        if element_idx + 1 < len(arrs[array_idx]):
            next_element = arrs[array_idx][element_idx + 1]
            heapq.heappush(min_heap, [next_element, array_idx, element_idx + 1])
        
    return merged_array
        

# Тест
def test_merge_k_sorted_arrays_1():
    test_arr = [[1, 3, 5, 7], [2, 4, 6], [0, 8, 9, 11]]
    assert merge_k_sorted_arrays_1(test_arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    return True

def test_merge_k_sorted_arrays_2():
    test_arr = [[1, 3, 5, 7], [2, 4, 6], [0, 8, 9, 11]]
    assert merge_k_sorted_arrays_2(test_arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    return True

print(test_merge_k_sorted_arrays_1())
print(test_merge_k_sorted_arrays_2())