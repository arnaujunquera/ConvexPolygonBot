import os
import sys
import inspect
from Polygons import ConvexPolygon
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


if __name__ is not None and "." in __name__:
    from .PolygonParser import PolygonParser
    from .PolygonVisitor import PolygonVisitor
else:
    from PolygonParser import PolygonParser
    from PolygonVisitor import PolygonVisitor


class EvalPolygon(PolygonVisitor):

    def __init__(self):
        self.dictionaryPolygons = {}

    # Reset dictionary
    def cleanDictionary(self):
        self.dictionaryPolygons = {}

    # Returns all the polygons
    def getPolygons(self):
        res = ""
        for key, value in self.dictionaryPolygons.items():
            res += str(key) + ': ' + value.toString() + "\n"
        if res == "":
            res = "No hi ha cap polígon desat"
        return res

    # Visit a parse tree produced by PolygonParser#root.
    def visitRoot(self, ctx: PolygonParser.RootContext):
        l = [n for n in ctx.getChildren()]
        return self.visit(l[0])

    # Visit a parse tree produced by PolygonParser#expr.
    def visitExpr(self, ctx: PolygonParser.ExprContext):
        l = [n for n in ctx.getChildren()]
        response = self.visit(l[0])
        if type(response) == ConvexPolygon:
            response = response.toString()
        elif type(response) == float:
            response = "{:.3f}".format(response)
        elif type(response) == bool:
            if response:
                response = "yes"
            else:
                response = "no"
        return response

    # Visit a parse tree produced by PolygonParser#assign.
    def visitAssign(self, ctx: PolygonParser.AssignContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.visit(l[2])
        ide = l[0].getText()
        self.dictionaryPolygons[ide] = polygon
        # return polygon

    # Visit a parse tree produced by PolygonParser#clause.
    def visitClause(self, ctx: PolygonParser.ClauseContext):

        l = [n for n in ctx.getChildren()]
        polygon = None
        if len(l) == 1:

            polygon = self.visit(l[0])
        elif len(l) == 3 and l[0].getText() == '(':
            polygon = self.visit(l[1])
        elif len(l) == 3:
            if self.visit(l[1]).getText() == ' * ':
                pol1 = self.visit(l[0])
                pol2 = self.visit(l[2])
                polygon = ConvexPolygon.getIntersection(pol1, pol2)
            elif self.visit(l[1]).getText() == ' + ':
                pol1 = self.visit(l[0])
                pol2 = self.visit(l[2])
                polygon = ConvexPolygon.getUnion(pol1, pol2)
        if len(l) == 2:
            if self.visit(l[0]).getText() == '#':
                polygon = ConvexPolygon(ConvexPolygon.getBoundingBox(self.visit(l[1]).points))
        return polygon

    # Visit a parse tree produced by PolygonParser#operbox.
    def visitOperbox(self, ctx: PolygonParser.OperboxContext):
        l = [n for n in ctx.getChildren()]
        return l[0]

    # Visit a parse tree produced by PolygonParser#polygon.
    def visitPolygon(self, ctx: PolygonParser.PolygonContext):
        l = [n for n in ctx.getChildren()]
        listPol = self.visit(l[0])
        if type(listPol) != ConvexPolygon:
            polygon = ConvexPolygon(listPol)
        else:
            polygon = listPol
        return polygon

    # Visit a parse tree produced by PolygonParser#variable.
    def visitVariable(self, ctx: PolygonParser.VariableContext):
        l = [n for n in ctx.getChildren()]
        ide = l[0].getText()
        polygon = self.dictionaryPolygons[ide]
        return polygon

    # Visit a parse tree produced by PolygonParser#point.
    def visitPoint(self, ctx: PolygonParser.PointContext):
        l = [n for n in ctx.getChildren()]
        x = float(l[0].getText())
        y = float(l[2].getText())
        listPoints = [(x, y)]
        return listPoints

    # Visit a parse tree produced by PolygonParser#compound.
    def visitCompound(self, ctx: PolygonParser.CompoundContext):
        l = [n for n in ctx.getChildren()]
        listPoints = []
        point = self.visit(l[1])
        listPoints.extend(point)
        point = self.visit(l[2])
        listPoints.extend(point)
        return listPoints

    # Visit a parse tree produced by PolygonParser#morePoints.
    def visitMorePoints(self, ctx: PolygonParser.MorePointsContext):
        l = [n for n in ctx.getChildren()]
        listPoints = []
        if len(l) > 0:
            point = self.visit(l[1])
            listPoints.extend(point)
            morePoints = self.visit(l[2])
            listPoints.extend(morePoints)
        return listPoints

    # Visit a parse tree produced by PolygonParser#opers.
    def visitOpers(self, ctx: PolygonParser.OpersContext):
        l = [n for n in ctx.getChildren()]
        return l[0]

    # Visit a parse tree produced by PolygonParser#printer.
    def visitPrinter(self, ctx: PolygonParser.PrinterContext):
        l = [n for n in ctx.getChildren()]
        res = ""
        if len(l) > 0:
            if len(l) == 4:
                res = l[2].getText()
            elif len(l) == 2:
                res = self.visit(l[1])
        return res

    # Visit a parse tree produced by PolygonParser#area.
    def visitArea(self, ctx: PolygonParser.AreaContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.visit(l[1])
        area = polygon.getArea()
        return float(area)

    # Visit a parse tree produced by PolygonParser#perimeter.
    def visitPerimeter(self, ctx: PolygonParser.PerimeterContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.visit(l[1])
        perimeter = polygon.getPerimeter()
        return float(perimeter)

    # Visit a parse tree produced by PolygonParser#vertices.
    def visitVertices(self, ctx: PolygonParser.VerticesContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.visit(l[1])
        vertices = polygon.getNumVertices()
        return vertices

    # Visit a parse tree produced by PolygonParser#centroid.
    def visitCentroid(self, ctx: PolygonParser.CentroidContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.visit(l[1])
        center = polygon.getCenterCoord()
        center = str(center[0]) + " " + str(center[1])
        return center

    # Visit a parse tree produced by PolygonParser#color.
    def visitColor(self, ctx: PolygonParser.ColorContext):
        l = [n for n in ctx.getChildren()]
        polygon = self.dictionaryPolygons[l[1].getText()]
        r = float(l[4].getText())
        g = float(l[6].getText())
        b = float(l[8].getText())
        polygon.setColor((r, g, b))
        return None

    # Visit a parse tree produced by PolygonParser#equal.
    def visitEqual(self, ctx: PolygonParser.EqualContext):
        l = [n for n in ctx.getChildren()]
        polygon1 = self.visit(l[1])
        polygon2 = self.visit(l[3])
        return ConvexPolygon.comparePolygons(polygon1, polygon2)

    # Visit a parse tree produced by PolygonParser#draw.
    def visitDraw(self, ctx: PolygonParser.DrawContext):
        l = [n for n in ctx.getChildren()]
        directory = l[2].getText()
        listPolygons = self.visit(l[4])
        ConvexPolygon.drawPolygons(directory, listPolygons)
        return directory

    # Visit a parse tree produced by PolygonParser#polygons.
    def visitPolygons(self, ctx: PolygonParser.PolygonsContext):
        l = [n for n in ctx.getChildren()]
        listPol = []
        if len(l) > 0:
            ide = l[1].getText()
            listPol.append(self.dictionaryPolygons[l[1].getText()])
            morePol = self.visit(l[2])
            listPol += morePol
        return listPol

    # Visit a parse tree produced by PolygonParser#moreIDE.
    def visitMoreIDE(self, ctx: PolygonParser.MoreIDEContext):
        l = [n for n in ctx.getChildren()]
        listPol = []
        if len(l) > 0:
            ide = l[1].getText()
            listPol.append(self.dictionaryPolygons[l[1].getText()])
            morePol = self.visit(l[2])
            listPol += morePol
        return listPol

    # Visit a parse tree produced by PolygonParser#calc.
    def visitCalc(self, ctx: PolygonParser.CalcContext):
        l = [n for n in ctx.getChildren()]
        resp = None
        if len(l) == 1:
            resp = self.visit(l[0])
        if len(l) == 2:
            resp = self.visit(l[0])
            listPolygons = self.visit(l[1])
            ConvexPolygon.drawPolygons(resp, listPolygons)
        return resp

    # Visit a parse tree produced by PolygonParser#random.
    def visitRandom(self, ctx: PolygonParser.RandomContext):
        l = [n for n in ctx.getChildren()]
        return ConvexPolygon.getRandomPolygon(int(l[1].getText()))

    # Visit a parse tree produced by PolygonParser#inside.
    def visitInside(self, ctx: PolygonParser.InsideContext):
        l = [n for n in ctx.getChildren()]
        pol1 = self.visit(l[1])
        pol2 = self.visit(l[3])
        polygon = pol2.polygonIsInside(pol1)
        return polygon
