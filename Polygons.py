import math
import functools
import random
from copy import copy
from PIL import Image, ImageDraw


class ConvexPolygon:
    def __init__(self, points):
        points = [ConvexPolygon.__rounder(xs) for xs in points]
        self.points = ConvexPolygon.getConvexHull(points)  # if the polygon is not convex, the unwanted points will be removed
        self.color = (100, 100, 100)

    def polygonIsInside(self, polygon):
        # Checks whether a convex polygon is inside another convex polygon.
        n = len(polygon.points)
        for i in range(0, n):
            if (not self.pointIsInside(polygon.points[i])):
                return False
        return True

    def getNumVertices(self):
        # Gets the number of vertices and edges (same) of a convex polygon.
        return len(self.points)

    def getPerimeter(self):
        # Gets the length of the perimeter of a convex polygon by summing the length of all the segments.
        n = len(self.points)
        suma = 0.0
        for i in range(0, n):
            p1 = self.points[i]
            p2 = self.points[(i+1) % n]
            v = ConvexPolygon.__getSegment(p1, p2)
            suma += math.sqrt(v[0]**2+v[1]**2)
        return round(suma, 3)

    def getArea(self):
        # Gets the area of a convex polygon by summing the area of the triangles created connecting one vertex to the others.
        n = len(self.points)
        p0 = self.points[0]
        area = 0.0
        for i in range(1, n-1):
            p1 = self.points[1]
            p2 = self.points[2]
            area += self.getTriangleArea(p0, p1, p2)
        return round(area, 3)

    def getCenterCoord(self):
        # Gets the coordinates of the centroid of a convex polygon.
        n = len(self.points)
        x = 0
        y = 0
        for i in range(0, n):
            x += self.points[i][0]
            y += self.points[i][1]
        x = x/n
        y = y/n
        return (round(x, 3), round(y, 3))

    def isRegular(self):
        # Checks if a convex polygon is regular by checking if the centroid distance to all the vertices is the same.
        c = self.getCenterCoord()
        r = ConvexPolygon.__getSegmentLength(ConvexPolygon.__getSegment(self.points[0], c))
        n = len(self.points)
        for i in range(0, n):
            if (ConvexPolygon.__getSegmentLength(ConvexPolygon.__getSegment(self.points[0], c)) != r):
                return False
        return True

    def getIntersection(polygon1, polygon2):
        # Computes the intersection of two convex polygons.
        # The points of the intersection polygon are the ones that are not part of the convex hull
        # and the ones created by the intersection of vectors
        conj = polygon1.points + polygon2.points
        hull = ConvexPolygon.getConvexHull(conj)
        inside = list(set(conj) ^ set(hull))
        intersected = ConvexPolygon.__getIntersectionPointsBetweenPolygons(polygon1, polygon2)
        newPoints = inside + intersected
        # If the points are not in the hull it means
        return ConvexPolygon(newPoints)

    def getUnion(polygon1, polygon2):
        # Computes the convex union of two convex polygons by computing the convex hull of all points of the two polygons.
        conj = polygon1.points + polygon2.points
        return ConvexPolygon(ConvexPolygon.getConvexHull(conj))

    def getBoundingBox(points):
        # Computes the bounding box of a convex polygon by checking the maximum and minimum coordinates.
        n = len(points)
        minx = points[0][0]
        miny = points[0][1]
        maxx = points[0][0]
        maxy = points[0][1]
        for i in range(1, n):
            if (points[i][0] < minx):
                minx = copy(points[i][0])
            if (points[i][0] > maxx):
                maxx = copy(points[i][0])
            if (points[i][1] < miny):
                miny = copy(points[i][1])
            if (points[i][1] > maxy):
                maxy = copy(points[i][1])
        return [(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)]

    def drawPolygons(dir, polygons):
        # Draws convex polygons (with colors) in a PNG image.
        auxpoints = []
        for p in polygons:
            auxpoints += p.points
        box = ConvexPolygon.getBoundingBox(auxpoints)

        h = ConvexPolygon.__getSegment(box[0], box[1])
        w = ConvexPolygon.__getSegment(box[0], box[3])

        minx = 0
        miny = 0

        if box[0][0] < 0:
            minx = box[0][0]*(-1)

        if box[0][1] < 0:
            miny = box[0][1]*(-1)
        h = ConvexPolygon.__getSegmentLength(h)
        w = ConvexPolygon.__getSegmentLength(w)
        n = round(max(h, w))

        scale = 397/n

        img = Image.new('RGB', (400, 400), 'White')
        dib = ImageDraw.Draw(img)
        for p in polygons:
            dpoints = copy(p.points)

            xs, ys = zip(*dpoints)
            dpointsx = list(map(lambda x: 1+(x+minx)*scale, xs))

            dpointsy = list(map(lambda y: 398-(y+miny)*scale, ys))
            dpoints = list(zip(dpointsx, dpointsy))
            dib.polygon(dpoints, None, p.color)

            for cord in dpoints:
                dib.ellipse((cord[0]-1, cord[1]-1, cord[0]+1, cord[1]+1), p.color, p.color)
        img.save(dir)

    def comparePolygons(p1, p2):
        # Returns True if the two polygons are equal.
        return p1.points == p2.points

    def setColor(self, color):
        # Sets the color of teh polygon given a tuple of 3 floats between 0 and 1. Scaled to 255.
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        self.color = (r, g, b)

    # ÚTILS

    def getTriangleArea(self, p0, p1, p2):
        # Gets the area of a triangle determined by 3 points
        a = ConvexPolygon.__getSegmentLength(ConvexPolygon.__getSegment(p0, p1))
        b = ConvexPolygon.__getSegmentLength(ConvexPolygon.__getSegment(p1, p2))
        c = ConvexPolygon.__getSegmentLength(ConvexPolygon.__getSegment(p2, p0))
        sper = (a+b+c)/2
        area = math.sqrt(sper*(sper-a)*(sper-b)*(sper-c))
        return round(area, 3)

    def dotProduct(self, v1, v2):
        # Computes the dot product of 2 vectors
        return v1[0]*v2[0]+v1[1]*v2[1]

    def __getSegment(p1, p2):
        # Returns de segment between 2 points
        return (p2[0]-p1[0], p2[1]-p1[1])

    def __getSegmentLength(v):
        # Returns the length of a segment
        return math.sqrt(v[0]**2+v[1]**2)

    def __getIntersectionPointsBetweenPolygons(polygon1, polygon2):
        # Returns the intersection between the segments of two polygons
        res = []
        n = len(polygon1.points)
        seg1 = []
        for i in range(0, n):
            seg1.append(((polygon1.points[i][0], polygon1.points[i][1]), (polygon1.points[(i+1) % n][0], polygon1.points[(i+1) % n][1])))  # (A, B)= ((x1, y1), (x2, y2))

        n = len(polygon2.points)
        seg2 = []
        for i in range(0, n):
            seg2.append(((polygon2.points[i][0], polygon2.points[i][1]), (polygon2.points[(i+1) % n][0], polygon2.points[(i+1) % n][1])))

        for s1 in seg1:
            for s2 in seg2:
                inters = ConvexPolygon.__getIntersectionBetweenSegments(s1, s2)
                if inters is not None:
                    res.append(inters)
        return res

    def __getIntersectionBetweenSegments(s1, s2):
        # Returns the intersection point between two segments.
        xdiff = (s1[0][0] - s1[1][0], s2[0][0] - s2[1][0])
        ydiff = (s1[0][1] - s1[1][1], s2[0][1] - s2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(*s1), det(*s2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        if x == -0:
            x = 0.000
        if y == -0:
            y = 0.000
        return x, y

    def getConvexHull(points):
        # Computes the convex hull of a set of points by using the Graham Scan algorithm
        # The algorithm creates the convex hull by visiting recursively all the points
        # If a set of three points creates a concave angle, the midle one is dismisssed
        def convex(p, q, r):
            a = (q[0] - p[0])*(r[1] - p[1])
            b = (r[0] - p[0])*(q[1] - p[1])
            res = a - b
            return (res > 0) - (res < 0)

        def _right(hull, r):
                while len(hull) > 1 and convex(hull[-2], hull[-1], r) != -1:
                        hull.pop()
                if not len(hull) or hull[-1] != r:
                        hull.append(r)
                return hull

        points = sorted(points)
        l = functools.reduce(_right, points, [])
        u = functools.reduce(_right, reversed(points), [])
        return l.extend(u[i] for i in range(1, len(u) - 1)) or l

    def getRandomPolygon(n):
        # Builds a polygon out of n random generated points.
        # The resulting polygon may contain less points because points inside the convex hull will be eliminated
        px = [random.uniform(0, 1) for i in range(n)]
        py = [random.uniform(0, 1) for i in range(n)]
        p = list(zip(px, py))
        return ConvexPolygon(p)

    def toString(self):
        # Returns the polygon points with string format
        pstr = ""
        for p in self.points:
                pstr += "{:.3f}".format(round(p[0], 3))
                pstr += " "
                pstr += "{:.3f}".format(round(p[1], 3))
                pstr += " "
        return pstr

    def getAngle(self, v1, v2):
        # Returns the angle between two vectors
        v1DOTv2 = self.dotProduct(v1, v2)
        v1Mag = math.sqrt(v1[0]**2+v1[1]**2)
        v2Mag = math.sqrt(v2[0]**2+v2[1]**2)
        ang = v1DOTv2/(v1Mag*v2Mag)
        ang = math.acos(ang)
        return ang*180/math.pi

    def __rounder(tup):
        # Rounds the point components to 3 decimals
        return (round(float(tup[0]), 3), round(float(tup[1]), 3))

    def pointIsInside(self, p):
        # Check whether a point is inside another convex polygon
        newHull = copy(self.points)
        newHull.append(p)
        checkHull = ConvexPolygon.getConvexHull(newHull)
        if (p in checkHull):
            return False
        else:
            return True
