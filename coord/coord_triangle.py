import math


def length(v0, v1):
    return math.sqrt(math.pow(v0[1] - v1[1], 2) + math.pow(v0[0] - v1[0], 2))


def slope(v0, v1):
    return (v0[1] - v1[1]) / (v0[0] - v1[0])


def midpoint(v0, v1):
    return (v0[0] + v1[0]) / 2., (v0[1] + v1[1]) / 2.


class CoordinateTriangle:

    def __init__(self, v0=(0, 0), v1=(0, 0), v2=(0, 0)):
        self.v0, self.v1, self.v2 = v0, v1, v2

    def area(self):
        return abs((self.v0[0] * (self.v1[1] - self.v2[1])
                    + self.v1[0] * (self.v2[1] - self.v0[1])
                    + self.v2[0] * (self.v0[1] - self.v1[1])
                    ) / 2.)

    def perimeter(self):
        return length(self.v0, self.v1) + length(self.v1, self.v2) + length(self.v2, self.v0)

    def centroid(self):
        return (self.v0[0] + self.v1[0] + self.v2[0]) / 3, (self.v0[1] + self.v1[1] + self.v2[1]) / 3

    def circumcenter(self):
        v0, v1, v2 = self.v0, self.v1, self.v2

        while v0[0] == v1[0] or v0[0] == v2[0]:
            v1, v2, v0 = v0, v1, v2

        midpoint_ab = midpoint(v0, v1)
        midpoint_ac = midpoint(v0, v2)

        slope_p_ab = -1. / slope(v0, v1)
        slope_p_ac = -1. / slope(v0, v2)

        y_int_p_ab = midpoint_ab[1] - slope_p_ab * midpoint_ab[0]
        y_int_p_ac = midpoint_ac[1] - slope_p_ac * midpoint_ac[0]

        x = (y_int_p_ab - y_int_p_ac) / (slope_p_ac - slope_p_ab)
        y = x * slope_p_ab + y_int_p_ab

        return x, y

    def orthocenter(self):
        v0, v1, v2 = self.v0, self.v1, self.v2

        while v0[0] == v1[0] or v1[0] == v2[0]:
            v1, v2, v1 = v0, v1, v2

        slope_p_ab = -1. / slope(v0, v1)
        slope_p_bc = -1. / slope(v1, v2)

        y_int_p_ab_v2 = v2[1] - slope_p_ab * v2[0]
        y_int_p_bc_v0 = v0[1] - slope_p_bc * v0[0]

        x = (y_int_p_ab_v2 - y_int_p_bc_v0) / (slope_p_bc - slope_p_ab)
        y = slope_p_ab * x + y_int_p_ab_v2

        return x, y

    def incenter(self):
        x = (length(self.v1, self.v2) * self.v0[0] + length(self.v0, self.v2) * self.v1[0] + length(self.v0, self.v1) * self.v2[0]) / self.perimeter()
        y = (length(self.v1, self.v2) * self.v0[1] + length(self.v0, self.v2) * self.v1[1] + length(self.v0, self.v1) * self.v2[1]) / self.perimeter()

        return x, y


if __name__ == "__main__":
    a = float(input('Enter x for a = (x, y): ')), float(input('Enter y for a = (x, y): '))
    b = float(input('Enter x for b = (x, y): ')), float(input('Enter y for b = (x, y): '))
    c = float(input('Enter x for c = (x, y): ')), float(input('Enter y for c = (x, y): '))

    triangle0 = CoordinateTriangle(a, b, c)
    print('Area: ' + str(triangle0.area()) + '\n')
    print('Length ab: ' + str(length(triangle0.v0, triangle0.v1)))
    if a[0] == b[0]:
        print('Slope ab: Undefined')
    else:
        print('Slope ab: ' + str(slope(triangle0.v0, triangle0.v1)))
    print('Midpoint ab: ' + str(midpoint(triangle0.v0, triangle0.v1)) + '\n')
    print('Length ac: ' + str(length(triangle0.v0, triangle0.v2)))
    if a[0] == c[0]:
        print('Slope ac: Undefined')
    else:
        print('Slope ac: ' + str(slope(triangle0.v0, triangle0.v2)))
    print('Midpoint ac: ' + str(midpoint(triangle0.v0, triangle0.v2)) + '\n')
    print('Length bc: ' + str(length(triangle0.v1, triangle0.v2)))
    if b[0] == c[0]:
        print('Slope bc: Undefined')
    else:
        print('Slope bc: ' + str(slope(triangle0.v1, triangle0.v2)))
    print('Midpoint bc: ' + str(midpoint(triangle0.v1, triangle0.v2)) + '\n')
    print('Perimeter: ' + str(triangle0.perimeter()) + '\n')
    print('Centroid: ' + str(triangle0.centroid()))
    print('Circumcenter: ' + str(triangle0.circumcenter()))
    print('Orthocenter: ' + str(triangle0.orthocenter()))
    print('Incenter: ' + str(triangle0.incenter()))
