import torch
import time

cuda = torch.device('cuda')

y = torch.full((10000, 10000), 10000, device=cuda)
z = torch.full((10000, 10000), 10000, device=cuda)

start = time.time()

dot = torch.mm(y, z)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print(dot)

y = torch.full((10000, 10000), 10000)
z = torch.full((10000, 10000), 10000)

start = time.time()

dot = torch.mm(y, z)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print(dot)
