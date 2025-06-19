import math
import random

seed_num = int(input())
random.seed(seed_num)

hits = 0

for i in range(10000):
    theta = random.randint(0,180)
    D = random.uniform(0, 0.5)
    if D <=0.5*math.sin(math.radians(theta)):
        hits += 1

approximation = 2*10000.0/float(hits)




print(f'{approximation:.6f}')
