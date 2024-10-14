import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([50,30,25,65,10])
# y=np.array(["orange","pineapple","apple","mango","pomogranate"])
# plt.title("Types and Number of Plants")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.bar(y, x)
# plt.show()


k=1
for i in range(0,5):
     for j in range(0,i+1):
             print(k,end=" ")
             k=k+1
     print()