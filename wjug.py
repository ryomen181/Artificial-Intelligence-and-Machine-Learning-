#Water jug is a AI search problem which divides a big problem into small states, apply rules to move in between, and logically reach the goal state
# Water Jug Problem
# Jug X capacity = 4 litres (m)
# Jug Y capacity = 3 litres (n)
# Goal: Get exactly 2 litres in jug X using rules

x = 0
y = 0
m = 4
n = 3

print("Initial state = (0,0)")
print("Capacities = (4,3)")
print("Goal state = (2,y)")

# Loop until jug X contains exactly 2 litres
while (x != 2):

    r = int(input("Enter the rule: "))

    if (r == 1):
        # Fill jug X completely
        x = m

    elif (r == 2):
        # Fill jug Y completely
        y = n

    elif (r == 3):
        # Empty jug X
        x = 0

    elif (r == 4):
        # Empty jug Y
        y = 0

    elif (r == 5):
        # Pour water from X → Y until Y is full
        t = n - y
        y = n
        x -= t

    elif (r == 6):
        # Pour water from Y → X until X is full
        t = m - x
        x = m
        y -= t

    elif (r == 7):
        # Move all water from X into Y
        y += x
        x = 0

    elif (r == 8):
        # Move all water from Y into X
        x += y
        y = 0

    else:
        print("Invalid rule")

    print("Current State:", x, y)
