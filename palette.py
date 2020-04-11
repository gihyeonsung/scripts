#!/usr/bin/env python3

normBegin, brigBegin = 40, 100

def printBlock(color: int):
    print('\x1B[' + str(color) + 'm  \x1B[0m', end='')

# Print background color and 8 normal colors
printBlock(49)
for c in range(normBegin, normBegin + 8):
    printBlock(c)
print()

# Print foreground color and 8 bright colors
printBlock(107)
for c in range(brigBegin, brigBegin + 8):
    printBlock(c)
print()
