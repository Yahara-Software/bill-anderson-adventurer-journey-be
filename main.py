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
digits="0123456789"
directions="FBLR"

for char in instructions:
    if char in digits:
        num += char
        
    elif char in directions:
        if num == "":
            raise Exception("Cannot provide direction " + char + " without preceding it with a number.")

        num = int(num);
        
        if char == "F":
            y += num
        
        elif char == "B":
            y -= num
        
        elif char == "L":
            x -= num
        
        elif char == "R":
            x += num
            
        num = ""


dist = math.sqrt(x * x + y * y)
print("Distance between starting point and ending point: " + str(dist))

