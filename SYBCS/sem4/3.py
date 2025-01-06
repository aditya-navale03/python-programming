#write a program to sort a tuple using lambda 
#original list of tuple.
#[(english,88),(science,90),(math,97),(social science, 82)]
#sort the list of tuple.
#[(social science,82),(english, 88),(science, 90),(math, 97)]

subject_Marks = [('English',88),('science',90),('math',97),('social science',82)]
sorted_items = sorted(subject_Marks, key = lambda x:x[1])
print(sorted_items)