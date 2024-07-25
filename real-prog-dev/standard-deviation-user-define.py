#standard deviation
dataset = [12,3,34,5,5,23,23,4,34]
def calculate(dataset):
    mean = len(dataset) / sum(dataset)
    variance = sum((i - mean) ** 2 for i in  dataset) / len(dataset)
    standard_dev = variance ** 0.5
    return standard_dev

calculate(dataset)



