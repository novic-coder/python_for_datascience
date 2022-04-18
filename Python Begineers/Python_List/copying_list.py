import copy

original_list = [1,2,3,4]
copy_list = original_list
print(original_list)
print(copy_list)
copy_list[0]=5
print(original_list)

# It made changes to the original list also we call it shallow copying

# ways to copy the lists

# Using copy method
original_list = [10,20,30,40]
copy_list = original_list.copy()
copy_list[0]=5
print(original_list)
print(copy_list)


# using Slicing operator
my_list = [100,200,300,400]
your_list = my_list[:]
your_list[0]=50
print(my_list)
print(your_list)

even_list =[4,6,8,10,12]
# using list function
even_list1 = list(even_list)
even_list1[0]=2
print(even_list1)

# using copy function

even_list2 = copy.copy(even_list)
even_list2[0]=2
print(even_list2)
print(even_list)

# using deep copy

even_list3 = copy.deepcopy(even_list)
even_list3[0]=2
print(even_list3)
print(even_list)

