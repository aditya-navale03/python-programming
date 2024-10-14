# # # from turtle import *
# # # import colorsys
# # # bgcolor("black")
# # # tracer(41)
# # # h = 0
# # # goto(-110, 200)
# # # for i in range(9999999):
# # #      c = colorsys.hsv_to_rgb(h, 1, 1)
# # #      fillcolor(c)
# # #      begin_fill()
# # #      lt(119)
# # #      circle(50)
# # #      circle(50)
# # #      circle(20)
# # #      backward(350 - i)  
# # #      end_fill()
# # #      h += 0.005

# # # # import turtle

# # # # turtle.bgcolor("black")
# # # # squary = turtle.Turtle()
# # # # squary.speed(20)
# # # # squary.pencolor("red")
# # # # turtle.shape("turtle")

# # # # for t in range(40):
# # # #      squary.forward(t)
# # # #      squary.right(91)  
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width
    
# #     def area(self):
# #         return self.length * self.width
    
   

# #     def perimeter(self):
# #         return 2 * (self.length + self.width)


# # r = Rectangle(10, 5)  

# # print("Area:", r.area())
# # print("Perimeter:", r.perimeter())

# def product(a, b):
#     print(a * b)
# def product(a, b, c):
#     print(a * b * c)
# product(5, 6, 3)
# product(5 ,6 ,7)

import requests
import json

# Define the API endpoint
url = "http://fenixservices.fao.org/faostat/api/v1/en/data/QC/production"

# Set the query parameters
params = {
    "area": 231,   # United States
    "item": 15,    # Wheat
    "year": 2020,  # Year 2020
    "format": "json"  # Response format in JSON
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Print the data in a readable format
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
