%{
int flag=0;
int display(int x, char *y); 
%}

%%

(int|float|string|char|new) {flag = 0; display(flag, yytext);} 
[A-Za-z][A-Za-z0-9]* {flag = 1; display(flag, yytext);}
[,;] {flag = 2; display(flag, yytext);}
[+-/*=><] {flag = 3; display(flag, yytext);}
.[-]*[0-9]+ {flag = 4; display(flag, yytext);}

%%

int yywrap(){return 0;}

int main(){
printf("Enter i/p character \n");
yylex(); }
int display(int a, char *c){ if(flag==0){
printf("\n%s is a keyword",c); }else if(flag==2){
printf("\n%s is a separator",c); }else if(flag==3){
printf("\n%s is a operator",c); }else if(flag==4){
printf("\n%s is a constant",c); }else if(flag==1){
printf("\n%s is identifier", c); }
return 0;
}