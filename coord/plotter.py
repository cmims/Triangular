import matplotlib.pyplot as plt
import coord.coord_triangle as tri


if __name__ == "__main__":
    a = float(input('Enter x for a = (x, y): ')), float(input('Enter y for a = (x, y): '))
    b = float(input('Enter x for b = (x, y): ')), float(input('Enter y for b = (x, y): '))
    c = float(input('Enter x for c = (x, y): ')), float(input('Enter y for c = (x, y): '))

    triangle0 = tri.CoordinateTriangle(a, b, c)

    plt.plot([triangle0.v0[0], triangle0.v1[0]], [triangle0.v0[1], triangle0.v1[1]])
    plt.plot([triangle0.v1[0], triangle0.v2[0]], [triangle0.v1[1], triangle0.v2[1]])
    plt.plot([triangle0.v2[0], triangle0.v0[0]], [triangle0.v2[1], triangle0.v0[1]])

    plt.scatter([triangle0.v0[0], triangle0.v1[0], triangle0.v2[0]],
                [triangle0.v0[1], triangle0.v1[1], triangle0.v2[1]])
    plt.annotate('A ' + str(triangle0.v0), [triangle0.v0[0], triangle0.v0[1]])
    plt.annotate('B ' + str(triangle0.v1), [triangle0.v1[0], triangle0.v1[1]])
    plt.annotate('C ' + str(triangle0.v2), [triangle0.v2[0], triangle0.v2[1]])

    centroid = triangle0.centroid()
    circumcenter = triangle0.circumcenter()
    orthocenter = triangle0.orthocenter()
    incenter = triangle0.incenter()

    plt.scatter(centroid[0], centroid[1])
    plt.scatter(circumcenter[0], circumcenter[1])
    plt.scatter(orthocenter[0], orthocenter[1])
    plt.scatter(incenter[0], incenter[1])

    plt.annotate('Centroid ' + str(centroid), [centroid[0], centroid[1]])
    plt.annotate('Circumcenter ' + str(circumcenter), [circumcenter[0], circumcenter[1]])
    plt.annotate('Orthocenter ' + str(orthocenter), [orthocenter[0], orthocenter[1]])
    plt.annotate('Incenter ' + str(incenter), [incenter[0], incenter[1]])

    plt.show()