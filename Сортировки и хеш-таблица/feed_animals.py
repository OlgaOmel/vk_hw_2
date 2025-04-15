def feed_animals(animals,food):
    if len(animals) == 0 or len(food) == 0:
        return 0
   
    animals.sort()
    food.sort()
   
    count = 0
    for f in food:
        if len(animals) > count:
            if f >= animals[count]:
                count +=1
            if count == len(animals):
                break
    return count

# Тест
def test_feed_animals():
    test_animals = [8,2,3,2]
    test_food = [1,4,3,8]
    assert feed_animals(test_animals, test_food) == 3
    return True

test_feed_animals()
