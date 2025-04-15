def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            m_gap = i
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap-gap] = arr[m_gap-gap], arr[m_gap]
                m_gap -= gap
        gap = gap // 2
    return arr

# Тест
def test_shell_sort():
    test_arr = [1,10,5,2]
    assert shell_sort(test_arr) == [1, 2, 5, 10]
    return True

test_shell_sort()