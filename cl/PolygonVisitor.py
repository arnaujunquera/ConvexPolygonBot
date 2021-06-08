# Generated from Polygon.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PolygonParser import PolygonParser
else:
    from PolygonParser import PolygonParser

# This class defines a complete generic visitor for a parse tree produced by PolygonParser.

class PolygonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolygonParser#root.
    def visitRoot(self, ctx:PolygonParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#expr.
    def visitExpr(self, ctx:PolygonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#assign.
    def visitAssign(self, ctx:PolygonParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#printer.
    def visitPrinter(self, ctx:PolygonParser.PrinterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#clause.
    def visitClause(self, ctx:PolygonParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#polygons.
    def visitPolygons(self, ctx:PolygonParser.PolygonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#polygon.
    def visitPolygon(self, ctx:PolygonParser.PolygonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#variable.
    def visitVariable(self, ctx:PolygonParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#point.
    def visitPoint(self, ctx:PolygonParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#compound.
    def visitCompound(self, ctx:PolygonParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#morePoints.
    def visitMorePoints(self, ctx:PolygonParser.MorePointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#random.
    def visitRandom(self, ctx:PolygonParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#opers.
    def visitOpers(self, ctx:PolygonParser.OpersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#operbox.
    def visitOperbox(self, ctx:PolygonParser.OperboxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#opern.
    def visitOpern(self, ctx:PolygonParser.OpernContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#calc.
    def visitCalc(self, ctx:PolygonParser.CalcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#equal.
    def visitEqual(self, ctx:PolygonParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#inside.
    def visitInside(self, ctx:PolygonParser.InsideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#draw.
    def visitDraw(self, ctx:PolygonParser.DrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#directory.
    def visitDirectory(self, ctx:PolygonParser.DirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#moreIDE.
    def visitMoreIDE(self, ctx:PolygonParser.MoreIDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#color.
    def visitColor(self, ctx:PolygonParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#area.
    def visitArea(self, ctx:PolygonParser.AreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#perimeter.
    def visitPerimeter(self, ctx:PolygonParser.PerimeterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#vertices.
    def visitVertices(self, ctx:PolygonParser.VerticesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolygonParser#centroid.
    def visitCentroid(self, ctx:PolygonParser.CentroidContext):
        return self.visitChildren(ctx)



del PolygonParser