#userdefine harmonic mean
values = [1,2,3,4,4,3,2,4]
def h_mean(values):
    mean = len(values) / (1/values[0] + 1/values[1] + 1/values[2] + 1/values[3] + 1/values[4])
    return mean
