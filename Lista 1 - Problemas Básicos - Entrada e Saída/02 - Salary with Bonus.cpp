#include <iostream>
 
using namespace std;
 
int main() {
 
    float salario, vendas;
    
    scanf ("%s");
    scanf ("%f", &salario);
    scanf ("%f", &vendas);
    
    printf ("TOTAL = R$ %.2f\n", salario + (vendas * 0.15));
    
    return 0;
}