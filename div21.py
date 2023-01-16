import numpy as np
from scipy import stats
a = [12,36,57,88,11,36,3,57,94,78,77,85,36]
m1 = np.mean(a)
m2 = np.median(a)
m3 = stats.mode(a)
s = np.std(a)
print("Mean = ",m1)
print("Median = ",m2)
print("Mode = ",m3)
print("Standard Deviation = ",s)
