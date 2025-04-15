def anagram(strs):
    anagrams = {}
    
    for i in strs:
        sorted_i = ''.join(sorted(i))
        if sorted_i in anagrams:
            anagrams[sorted_i].append(i)
        else:
            anagrams[sorted_i] = [i]
    return list(anagrams.values())
        

# Тест
def test_anagram():
    test_arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    assert anagram(test_arr) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    return True

test_anagram()