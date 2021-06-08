import sys
from antlr4 import *
from PolygonLexer import PolygonLexer
from PolygonParser import PolygonParser
from PolygonVisitor import PolygonVisitor
from EvalPolygon import EvalPolygon

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
	input_stream = InputStream(input('? '))

visitor = EvalPolygon()
while input_stream != "..":
	

	lexer = PolygonLexer(input_stream)
	print(lexer)
	token_stream = CommonTokenStream(lexer)
	parser = PolygonParser(token_stream)
	tree = parser.root() 
	print(tree.toStringTree(recog=parser))
	visitor.visit(tree)
	input_stream = InputStream(input('? '))
	