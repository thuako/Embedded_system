import numpy as np

m = 8

a = ((np.binary_repr(-244, 7)[::-1])[:m])[::-1]

print(a, type(a))