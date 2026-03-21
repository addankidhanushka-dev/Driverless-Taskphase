coords = [(0,1), (0,3), (1,2)]

x_r = int(input("Enter the x co ordinate: "))
y_r = int(input("Enter th y co ordinate: "))

def distance_sq(point):
    x, y = point         # tuple unpacking
    return (x- x_r)**2 + (y- y_r)**2

sorted_coords = sorted(coords, key=distance_sq)     # automatically passes points to the fn

print("Sorted list: ", sorted_coords)









































































