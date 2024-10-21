import math

def polygon_area(num_sides, side_length):
    # Formula for area of a regular polygon: (n * s^2) / (4 * tan(pi / n))
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

# Example usage
num_sides = 4
side_length = 25

area = polygon_area(num_sides, side_length)
print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.0f}")
