#standard deviation userdefine
observation = [1,5,4,2,0]
sum = 0

for i in range(len(observation)):
    sum += observation[i]
    mean = sum / len(observation)

sum_of_squared_devaition = 0
for i in range(len(observation)):
    sum_of_squared_devaition += (observation[i] - mean) ** 2

standard_deviation = ((sum_of_squared_devaition) / len(observation)) ** 0.5
print("standard deviation of sample is:",standard_deviation)