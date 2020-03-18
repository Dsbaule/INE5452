#include <iostream>
 
using namespace std;
 
int main() {
 
    int A1, A2, A3, M1, M2, M3, best;

    scanf(" %d", &A1);
    scanf(" %d", &A2);
    scanf(" %d", &A3);

    M1 = (A2 * 2) + (A3 * 4);
    M2 = (A1 * 2) + (A3 * 2);
    M3 = (A1 * 4) + (A2 * 2);
    
    if(M1 <= M2){
        if(M1 <= M3)
            best = M1;
        else
            best = M3;
    } else {
        if(M2 <= M3)
            best = M2;
        else
            best = M3;
    }

    printf("%d\n", best);

    return 0;
}