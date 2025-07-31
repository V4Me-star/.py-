# 1. create an empty list called my-list.
my_list=[]

# 2. Append the following elements to my-list:10,20,30,40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending:{my_list}")

# 3.Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(f"After inserting 15 at second position:{my_list}")

# 4.Extend my_list with another list:[50,60,70]
my_list.extend([50,60,70])
print(f"After extending:{my_list}")

# 5.Remove the last element from my_list.
my_list=[10,20,30,40,50]
print(f"Original list:{my_list}")

#Remove the last element
my_list.pop()
print(f"List after removing the last element:{ my_list}")

# 6. Sort my_list in ascending order.
my_list.sort()
print(f"After sorting:{my_list}")

# 7. Find and print the index of the value 30 in my_list.
index_of_30=my_list.index(30)
print(f"The index of value 30 is:{index_of_30}")