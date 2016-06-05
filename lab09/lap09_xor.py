import numpy as np

xy = np.loadtxt('./train.txt', unpack=True)

x_data = xy[0:-1]
y_data = xy[-1]

print(x_data.shape)
print(x_data)

print(y_data)



