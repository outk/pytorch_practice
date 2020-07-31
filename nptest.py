import numpy as np
import time

start = time.time()

for i in range(10000):
    d1 = np.full((1000, 1000), 1000)
    d2 = np.full((1000, 1000), 1000)
    dsums = d1 + d2

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")