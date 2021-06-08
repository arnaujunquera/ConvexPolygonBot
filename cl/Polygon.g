grammar Polygon;
root : expr EOF ;

expr : ( assign | clause | printer | Comment | calc | color ) ;

assign : IDE ' := ' clause ;

printer : 
    | 'print ' clause
    | 'print ' IDE
    | 'print ' '"' String '"'
    ;

clause :
    | '(' clause ')'
    | '-' clause
    | clause opers clause
    | operbox clause
    | random
    | polygons
    | polygon
    ;
polygons :
    | ', ' polygon polygons
    ;
polygon :
    | variable
    | point
    | compound
    ;
    
variable : IDE ;

point : 
    | NUM ' ' NUM 
    ;

compound : '[' point morePoints ']' ;
morePoints : 
    | '  ' point morePoints
    ;
        
random : '!' NUM ;

opers : ( ' * ' | ' + ' ) ;
operbox : ( '#' ) ;

calc :
    | area
    | perimeter
    | vertices
    | centroid
    | equal
    | draw 
    | inside
    ;

equal : 
    | 'equal ' clause ', ' clause
    ;
inside :
    | 'inside ' clause ', ' clause
    ;
draw : 'draw ' '"' directory '"' clause;

directory: String '.png' ;

moreIDE : 
    | ', ' variable moreIDE
    ;

color : 'color ' IDE ', ' '{' NUM ' ' NUM ' ' NUM '}' ;
area : 'area ' clause ;
perimeter : 'perimeter ' clause ;
vertices : 'vertices ' clause ;
centroid : 'centroid ' clause ;


IDE    : [a-zA-Z][a-zA-Z0-9]*;
String : ('A'..'Z' | 'a'..'z' | '-' | '_' )+ ;
NUM    : (MINUS)? DIGIT+ ([.,] DIGIT+)? ;
MINUS : '-';
DIGIT : [0-9] ;     
Comment : '//' ~[\r\n]* -> skip ;

WS     : [ \n]+ -> skip ;
