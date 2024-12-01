import math

def circle_stats(radius) :
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

cal_area, cal_circumference = circle_stats(4)

# print("Area: ", cal_area, "Circumference: ", cal_circumference)
print(f"Area = {round(cal_area, 2)}\nCircumference = {round(cal_circumference, 2)}")