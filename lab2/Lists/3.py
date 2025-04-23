#Change list items
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

#Change Item Value - To change the value of a specific item, refer to the index number
list[1]="pineapple"
print(list)

#Change a Range of Item Values
list[-1:-3]=["tomato" , "potato"]
print(list)

#If you insert more items than you replace, 
# the new items will be inserted where you specified, and the remaining items will move accordingly:
list[1:2]=["carrot" , "cucumber" ]
print(list)
#The length of the list will change when the number of items inserted does not match the number of items replaced.

#Insert items - The insert() method inserts an item at the specified index:
list.insert(0, "cabbage")
print(list)
# As a result of the example above, the list will now contain 4 items. / получается мы тут не заменяем а добавляем

