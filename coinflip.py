# print("Hello", end=" ")
# print("World")

import random
from operator import is_not_none

for i in range(100):
    # Perform 100 coin flips
    if random.randint(0, 1) == 0:
        print("H", end=" ")
    else:
        print("T", end=" ")
print() # Print one newline at the end.
