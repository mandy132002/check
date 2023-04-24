%{
#include <stdio.h>
%}

%%
[aeiouAEIOU]    printf("%c is a vowel\n", yytext[0]);
.               printf("%c is a consonant\n", yytext[0]);
%%

int yywrap(){return 0;}

int main() {
    printf("Enter a character : ");
    yylex();
    return 0;
}