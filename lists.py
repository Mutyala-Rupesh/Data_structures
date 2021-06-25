list1 = [1,2,3,"hello"]

list1.append((2,0))
list1.extend((2,0))
list1.insert(3,"example")

print(list1)

del list1[3]
print(list1)

a = list1.pop(4)
print(a)

list1.remove(2)
print(list1)