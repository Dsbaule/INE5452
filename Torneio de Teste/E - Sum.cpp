#include <iostream>
 
using namespace std;
 
int main() {

    int num;
    scanf("%d", &num);

    if(num > 0) {
        float numGauss = (float)(num + 1);
        printf("%d\n", (int)(numGauss * ((numGauss - 1.0)/2.0)));        
    } else {
        float numGauss = (float)(-num + 1);
        printf("%d\n", (int)(-((numGauss * ((numGauss - 1.0)/2.0)) - 1)));    
    }
 
    return 0;
}