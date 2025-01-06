'''
write a program to find id a given string starts with a given character using lambda
sample output.
True 
False
'''

given_character = 'A'
character_string = 'Aditya'

answer = lambda x,y : x == y[0]
print(answer(given_character,character_string))