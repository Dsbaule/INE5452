#include <iostream>
 
using namespace std;
 
int main() {
 
    int num, atual, total = 0, c = 0, r = 0, s = 0;
    char type;
    
    scanf("%d", &num);
    
    for(int i = 0; i < num; i++) {
        scanf("%d %c", &atual, &type);
        total += atual;
        if(type == 'C')
            c += atual;
        else if(type == 'R')
            r += atual;
        else
            s += atual;
    }
    
    /*
    Total: 92 cobaias
    Total de coelhos: 29
    Total de ratos: 40
    Total de sapos: 23
    Percentual de coelhos: 31.52 %
    Percentual de ratos: 43.48 %
    Percentual de sapos: 25.00 %
    */
    
    printf("Total: %d cobaias\n", total);
    printf("Total de coelhos: %d\n", c);
    printf("Total de ratos: %d\n", r);
    printf("Total de sapos: %d\n", s);
    
    float percentC = ((float)c/(float)total) * 100.0;
    float percentR = ((float)r/(float)total) * 100.0;
    float percentS = ((float)s/(float)total) * 100.0;
    
    printf("Percentual de coelhos: %.2f %%\n", percentC);
    printf("Percentual de ratos: %.2f %%\n", percentR);
    printf("Percentual de sapos: %.2f %%\n", percentS);
 
    return 0;
}