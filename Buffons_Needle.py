import numpy as np
import random

# sets seed to input
num = int(input())
random.seed(num)

# Buffon's needle parameters
needle_length = 1.0
line_spacing = 1.0

hits = 0

for i in range(10000):
    theta = random.uniform(0, np.pi) # randomly generate an angle from 0 to 180 degrees
    extension = (needle_length/2) *np.sin(theta)
    D = random.uniform(0, line_spacing/2) # randomly generate a number from 0 to 0.5
    if extension >= D: # write condition for the needle hitting the line before the
        hits += 1

probability = hits/10000
if probability > 0:
    approximation = (2*needle_length)/(probability*line_spacing) # write formula for the approximation of pi
else:
    approximation = 0

#Expected with input 123 the output is 3.178134
print(f'{approximation:.6f}')