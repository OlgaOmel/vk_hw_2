def extra_letter(a, b):
    hash_map_b = {}

    for i in b:
        if i in hash_map_b:
            hash_map_b[i] += 1
        else:
            hash_map_b[i] = 1
            
    for i in a:
        if i in hash_map_b:
            hash_map_b[i] -= 1
            
    for k,v in hash_map_b.items():
        if v > 0:
            return k
               
    return ''

# Тест
def test_extra_letter():
    test_a = 'uio'
    test_b = 'oeiu'
    assert extra_letter(test_a,test_b) == 'e'
    return True

test_extra_letter()






















