import numpy as np
x = np.arange(10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 1
print (x[np.argsort(x)[-n:]])
