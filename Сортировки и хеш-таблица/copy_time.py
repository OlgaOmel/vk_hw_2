def copy_time(n,x,y):
    l = 0
    r = (n-1) * max(x,y)
    
    while l+1 < r:
        middle = (l+r) // 2
        if middle/x + middle/y > n-1:
            l = middle
        else:
            r = middle   
    return r+min(x,y)

# Тест
def test_copy_time():
    n_test=5
    x_test=1
    y_test=2
    assert copy_time(n_test,x_test,y_test) == 9
    return True

test_copy_time()
