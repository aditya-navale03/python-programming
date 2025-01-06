'''
write a python program to extract year , month, date and tiem using lambda function
sample output.
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
'''
from datetime import datetime

get_date_time = lambda:  datetime.now()
print(get_date_time())