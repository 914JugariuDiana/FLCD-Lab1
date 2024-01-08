%{
#include <stdio.h>
#include <string.h>
#include "test.tab.h"
int lines = 0;
%}

%option noyywrap
%option caseless

DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INT_CONSTANT [-]?{NON_ZERO_DIGIT}{DIGIT}*|0
LETTER [a-zA-Z_]
STRING_CONSTANT \"({LETTER}|{DIGIT})*\"
IDENTIFIER {LETTER}({LETTER}|{DIGIT})*
BAD_IDENTIFIER ({DIGIT})+({LETTER})+({LETTER}|{DIGIT})*

%%

"integer" { printf("%s - reserved word\n", yytext); return INTEGER; }
"string" { printf("%s - reserved word\n", yytext); return STRING; }
"boolean" { printf("%s - reserved word\n", yytext); return BOOLEAN; }
"char" { printf("%s - reserved word\n", yytext); return CHAR; }
"IF" { printf("%s - reserved word\n", yytext); return IF; }
"ELSE" { printf("%s - reserved word\n", yytext); return ELSE; }
"READ" { printf("%s - reserved word\n", yytext); return READ; }
"PRINT" { printf("%s - reserved word\n", yytext); return PRINT; }
"for" { printf("%s - reserved word\n", yytext); return FOR; }
"while" { printf("%s - reserved word\n", yytext); return WHILE; }
"length" { printf("%s - reserved word\n", yytext); return LENGTH; }

"+" { printf("%s - operator\n", yytext); return PLUS; }
"-" { printf("%s - operator\n", yytext); return MINUS; }
"*" { printf("%s - operator\n", yytext); return MULTIPLY; }
"/" { printf("%s - operator\n", yytext); return DIVIDE; }
"mod" { printf("%s - operator\n", yytext); return mod; }
"=" { printf("%s - operator\n", yytext); return ASSIGN; }
">" { printf("%s - operator\n", yytext); return GREATER; }
">=" { printf("%s - operator\n", yytext); return GEQ; }
"<" { printf("%s - operator\n", yytext); return LESSER; }
"<=" { printf("%s - operator\n", yytext); return LEQ; }
"==" { printf("%s - operator\n", yytext); return EQ; }
"!=" { printf("%s - operator\n", yytext); return NEQ; }
"^" { printf("%s - operator\n", yytext); return CARRAT; }
"and" { printf("%s - operator\n", yytext); return and; }
"or" { printf("%s - operator\n", yytext); return or; }

";" { printf("%s - separator\n", yytext); return SEMICOLON; }
"(" { printf("%s - separator\n", yytext); return ROUNDOB; }
")" { printf("%s - separator\n", yytext); return ROUNDCB; }
"[" { printf("%s - separator\n", yytext); return SQUAREOB; }
"]" { printf("%s - separator\n", yytext); return SQUARECB; }
"{" { printf("%s - separator\n", yytext); return CURLYOB; }
"}" { printf("%s - separator\n", yytext); return CURLYCB; }

{IDENTIFIER} {printf("%s - identifier\n", yytext); return id; }

{BAD_IDENTIFIER} {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

{INT_CONSTANT} {printf("%s - int constant\n", yytext); return constant; }

{STRING_CONSTANT} {printf("%s - str constant\n", yytext); return constant; }

[ \t]+ {}

[\n]+ {++lines;}

. {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

%%