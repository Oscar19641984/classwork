numbers = [15, 7, 3, 9] #list to find maximun number from

mid = len(numbers) // 2

list1 = numbers[:mid]
list2 = numbers[mid:]

print(list1)
print(list2)

mid = len(list1) // 2

list3 = list1[:mid]
list4 = list1[mid:]

print(list3)
print(list4)

mid = len(list2) // 2

list5 = list2[:mid]
list6 = list2[mid:]

print(list5)
print(list6)

if list3 > list4:
    max1 = list3
elif list3 < list4:
    max1 = list4

if list5 > list6:
    max2 = list5
elif list5 < list6:
    max2 = list5

if max1 > max2:
    newmax = max1
elif max1 < max2:
    newmax = max2

print(newmax)