#!/usr/bin/env python3

import sys
import math

if len(sys.argv) != 1:
    instructions = sys.argv[1]

else:
    instructions = "15F6B6B5L16R8B16F20L6F13F11R"


x = 0
y = 0
num=""

directions= {
    "F": lambda num, x, y : ("", x, y + int(num)),
    "B": lambda num, x, y : ("", x, y - int(num)),
    "L": lambda num, x, y : ("", x - int(num), y),
    "R": lambda num, x, y : ("", x + int(num), y)
}

for digit in range (0, 10):
    digit = str(digit)
    directions[digit] = lambda num, x, y, d=digit : (num + d, x, y)

for char in instructions:
    if char in directions:
        num, x, y = directions[char](num, x, y)
        
    else:
        raise Exception("Invalid character in instructions sequence: '" + char + "'")


dist = math.sqrt(x * x + y * y)
print("Distance between starting point and ending point: " + str(dist))

