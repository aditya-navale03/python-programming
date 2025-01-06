'''
write a python program to filter a list of integer using lambda
original list of integer.
[1,2,3,4,5,6,7,8,9,10]
even number from the said list.
[2,4,6,7,8,9]
odd number from the said list.
[1,3,5,7,9]
'''
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

even_list = list(filter(lambda x: x % 2 ==0,list_of_numbers))
print(even_list)

odd_list = list(filter(lambda x: x % 2 != 0,list_of_numbers))
print(odd_list)