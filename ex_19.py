tuple_my = ("one", "two", "three")

'''
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple.
'''

temp_list = list(tuple_my)
temp_list[0] = "new"
tuple_my = tuple(temp_list)

print(tuple_my)
