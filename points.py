import math
class Point:
    x_val=0.0
    y_val=0.0
    def __init__(self,x,y):
        self.x_val = x
        self.y_val = y

    # @x_val.setter
    def X_val(self,x):
        self.x_val = x
    
    # @y_val.setter
    def Y_val(self,y):
        self.y_val = y

    @property
    def X_get(self):
        return self.x_val

    @property
    def Y_get(self):
        return self.y_val

    def __str__(self):
        return "(" + str(self.x_val) + "," + str(self.y_val) + ")"

    def distance_from_point(self,the_other_point):
        dx = the_other_point.X_get - self.x_val
        dy = the_other_point.Y_get - self.y_val
        return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

    def slope(self,other_point):
        if self.x_val - other_point.X_get == 0 :
            return 0
        else:
            slope_val = (self.y_val - other_point.Y_get)/ (self.x_val - other_point.X_get)
            return slope_val


def main():
    print("Please Enter Coordinates of point 1:\n")
    x1 = float(input("x coordinate: "))
    y1 = float(input("y coordinate: "))
    p1 = Point(x1,y1)

    print("Please Enter Coordinates of point 2:\n")
    x2 = float(input("x coordinate: "))
    y2 = float(input("y coordinate: "))
    p2 = Point(x2,y2)

    print("Point 1 Coordinates ",p1.__str__())
    print("Point 2 Coordinates ",p2.__str__())

    d=p1.distance_from_point(p2)
    print("The Distance Between them is ",d)

    s=p1.slope(p2)
    print("The slope is ~",s)


main()
