%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token WRITE
%token ELSE
%token IF
%token PRINT
%token READ
%token FOR
%token WHILE

%token EQ
%token LEQ
%token GEQ
%token NEQ
%token GREATER
%token LESSER
%token ASSIGN

%token id
%token constant
%token nr

%token CHAR
%token INTEGER
%token BOOLEAN
%token STRING
%token FLOAT
%token LENGTH

%token ROUNDOB
%token ROUNDCB
%token SQUAREOB
%token SQUARECB
%token CURLYOB
%token CURLYCB
%token SEMICOLON

%left PLUS MINUS
%left DIV mod MULTIPLY
%left DIVIDE
%left CARRAT
%left or
%left and
%left NOT

%start program 

%%
program: stmt program {printf("program -> stmt program }\n");}
	|stmt {printf("program -> stmt }\n");}
stmt : declaration SEMICOLON {printf("stmt  -> declaration ; \n");} 
	|arraydecl SEMICOLON {printf("stmt  -> arraydecl ;\n");} 
	|assignstmt SEMICOLON{printf("stmt -> assignstmt ; \n");}
	|iostmt SEMICOLON {printf("stmt -> iostmt ;\n");} 
	|ifstmt {printf("stmt -> ifstmt\n");} 
	|whilestmt {printf("stmt -> whilestmt\n");} 
	|forstmt {printf("stmt -> forstmt\n");}


declaration : type1 id {printf("declaration  -> type1 id \n");}

type1 : BOOLEAN {printf("type1 -> boolean\n");} 
	|INTEGER {printf("type1 -> integer\n");} 
	|STRING {printf("type1 -> string\n");} 
	|CHAR {printf("type1 -> char\n");} 
	|FLOAT {printf("type1 -> float n");}


type : type1 {printf("type  -> type1\n");} 
	| arraydecl {printf("type  -> arraydecl \n");}

arraydecl : type1 id SQUAREOB constant SQUARECB {printf("arraydecl -> type1 id [constant]  \n");}

assignstmt : id ASSIGN expression {printf("assignstmt -> id = expression\n");}

expression : expression operator expression {printf("expression -> expression operator expression\n");} 
	| factor {printf("expression -> factor\n");}
	| LENGTH ROUNDOB expression ROUNDCB {printf("expression -> length(expression)\n");}

operator : PLUS	{printf("operator -> +\n");} 
	|MINUS {printf("operator -> -n");} 
	|MULTIPLY {printf("operator -> *\n");} 
	|DIVIDE {printf("operator -> /\n");} 	
	|mod {printf("operator -> mod\n");} 
	|CARRAT {printf("operator -> ^\n");} 

factor : id {printf("factor -> id\n");} 
	| constant {printf("factor -> constant\n");}

iostmt : READ ROUNDOB id ROUNDCB {printf("iostmt -> READ ( id )\n");} 
	| WRITE ROUNDOB id ROUNDCB {printf("iostmt -> WRITE ( id )\n");} 
	| PRINT ROUNDOB id ROUNDCB {printf("iostmt -> PRINT ( id )\n");}

ifstmt : IF ROUNDOB condition ROUNDCB CURLYOB program CURLYCB ELSE CURLYOB program CURLYCB {printf("ifstmt -> if ( condition ) { program } else { program }\n");}

whilestmt : WHILE ROUNDOB condition ROUNDCB CURLYOB program CURLYCB {printf("ifstmt -> while ( condition ) { program }\n");}

forstmt : FOR ROUNDOB assignstmt SEMICOLON condition SEMICOLON expression ROUNDCB CURLYOB program CURLYCB {printf("forstmt -> for ( assignstmt ; condition ; expression ) { program }\n");}

condition : expression relation expression {printf("condition -> expression relation expression\n");}
	|expression relation expression and expression relation expression {printf("condition -> expression relation expression and expression relation expression\n");}
	|expression relation expression or expression relation expression {printf("condition -> expression relation expression or expression relation expression\n");}

relation: LESSER {printf("relation -> <\n");}
	|LEQ {printf("relation -> <=\n");}
	|EQ {printf("relation -> ==\n");}
	|NEQ {printf("relation -> !=\n");}
	|GREATER {printf("relation -> >\n");}
	|GEQ {printf("relation >= <\n");}
%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin =  fopen(argv[1],"r");
	if(!yyparse()) fprintf(stderr, "\tOK\n");
} 