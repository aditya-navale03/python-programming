'''
write a python program to square and cube every number in a given list of integer using lambda.
original list of integer.
[1,2,3,4,5,6,7,8,9,10]
square every number of the said list.
[1,4,9,16,25,36,49,64,81,100]
cube every number of the said list.
[1,8,27,64,125,216,343,512,729,1000]
'''

list_of_number = [1,2,3,4,5,6,7,8,9,10]

square_number = list(map(lambda x: x ** 2,list_of_number))
cube_number = list(map(lambda x: x ** 3,list_of_number))

print(square_number)
print(cube_number)