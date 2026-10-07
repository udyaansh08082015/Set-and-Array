basket1= {"Mango","Lemon","Guava","Apple","Mango"}
basket2= {"Mango","Orange","Banana","Kiwi"}
print("Basket1:",basket1)
print("Basket2:",basket2)


basket1.add("orange")
print("Added fruit in basket one",basket1)


common_fruits= basket1.intersection(basket2)
print("Fruits in common",common_fruits)

import array as arr
fruits_count = arr.array("i",[3,5,2,4])
print(fruits_count)

fruits_count.insert(0,1)
fruits_count.append(7)
print("fruit count after adding items:",fruits_count)

count_of_four = fruits_count.count(4)
print("no. of fours",count_of_four)

fruits_count.reverse()
print("Reversed array fruit count ",fruits_count)

print("")
print("==========FRUIT BASKET ORGANIZER=========")
print("BASKET1",basket1)
print("BASKET2",basket2)
print("FRUITS COUNT",fruits_count)
print("==========================================")



