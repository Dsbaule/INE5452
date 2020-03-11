#include <iostream>
#include <cmath>
 
using namespace std;
 
int main() {
 
    float a, b, c;
    
    scanf("%f %f %f", &a, &b, &c);
    
    if(a == 0.0){
        printf("Impossivel calcular\n");
        return 0;
    }
    
    float delta = (b * b) - (4.0 * a * c);
    
    if(delta < 0.0){
        printf("Impossivel calcular\n");
        return 0;
    }
    
    float R1 = (-b + sqrt(delta))/(2.0 * a);
    float R2 = (-b - sqrt(delta))/(2.0 * a);
    
    printf("R1 = %.5f\nR2 = %.5f\n", R1, R2);
 
    return 0;
}