import random
from typing import Counter
"""
test_cases = input ("Cases: ")
R = input("R: ") # Shorter one
C = input("C: ") # Bigger one
x, y = 0
"""
grid = {}

def rows_creator(C):
    result = []
    for n in range(C):
        result.append(random.randrange(0, 2, 1))
    return result

def generate(R, C):
    for i in range(R):
        grid[i] = rows_creator(C)
    return grid

def rows(G, R):
    ones = {}
    for i in range(R):
        index = 0
        temp_list = []
        for item in G[i]: 
            if item == 1:
                temp_list.append(index)
            index += 1
        ones[i] = temp_list
    return ones
def lines_check(ones, R, C):
    for i in range(R):
        temp_list = ones[i]
        
def check(R, C, ones):
    for i in range(R):
        pass
def print_grid(G: dict, R):
    for i in range(R):
        print(G[i])
    print(rows(G, R))

print_grid(generate(3, 3), 3)
#print(f"Case #{x}: {y} ")