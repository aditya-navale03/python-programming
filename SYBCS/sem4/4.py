# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

mobile_model = [
    {
        'make':'Nokia','model':216,'color':'black'
    },
    {
        'make':'Mi max','model':2,'color':'gold'
    },
    {
        'make':'Samsung','model':7,'color':'blue'
    }
]

sorted_list= sorted(mobile_model, key = lambda x: x['color'])
print(sorted_list)