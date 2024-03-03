''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Iterate through all possible values of x and y '''
solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        # Check if the current x and y satisfy both equations
        if a*x + b*y == c and d*x + e*y == f:
            # Output the solution
            print(f'x = {x} , y = {y}')
            solution_found = True
            break  # Exit inner loop
    if solution_found:
        break  # Exit outer loop

# If no solution is found
if not solution_found:
    print('There is no solution')