# 1 Create a list with numbers 0 to 9 in it.
# 2 Display the list elements separated by a comma (comma at end ok)
# 3 Display all even elements of the list.
# 4 Display the average value of all elements in the list.

# Create the list
list1 = list(range(10))
even_list1 = list(range(0,10,2))
even_list2 = []

#del(list1[4])

# Display elements
for x in list1:
    print(str(x), end="")
    if x < max(list1):
        print(",", end="")

for x2 in list1:
    if x2 % 2 == 0:
        even_list2.append(x2)
        print(x2)

print(sum(list1)/len(list1))


print(even_list2)