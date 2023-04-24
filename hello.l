%{
char n[50];
%}
%%
\n {printf("Hello, %s!", n);}
%%
int yywrap() { return 0; }
int main(){
printf("\nWhat is your name?\n"); scanf("%s", n);
yylex();
return 0;
}
