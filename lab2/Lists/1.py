#Lists ([]) - Lists are used to store multiple items in a single variable.

#Allow duplicates - яғни листта қайталанатын элементтер бола бере алады

list1 = [ "banana" , "apple" , "banana" , "cherry" ]
print(list1)

#len() - қанша элемент бар екенін санайды, яғни ұзындығын
print(len(list1))

#data types - List items can be of any data type:

list2= [1,2,3,4,5]
print(list2)

#a list can contain diffferent data types
list3=[5, "cherry" , True]
print(list3)

#type()- From Python's perspective, lists are defined as objects with the data type 'list'
print(type(list3))

#list() constructor - It is also possible to use the list() constructor when creating a new list.

list4= list(("a" , "b" , "c"))
print(list4)