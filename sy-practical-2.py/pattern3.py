# A
# B B 
# C C C 
# D D D D
letters = 'ABCD'
for i in range(len(letters)):
    for j in range(0,i+1):
        print(letters[i],end=" ")
    print()