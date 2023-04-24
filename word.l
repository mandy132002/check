%{
#include <stdio.h>
%}

%%
[a-zA-Z]+    {printf("%s is a word\n",yytext );}
[0-9]+       {printf("%s is a number\n",yytext ) ; }
[a-zA-Z0-9]+ {printf("%s is a combination of word and number\n",yytext) ; }
.            {printf("%s is an invalid input\n",yytext ) ; }
%%

int yywrap(){return 0;}
int main(void){
    printf("Give some input");
    yylex();
    return 0;
}