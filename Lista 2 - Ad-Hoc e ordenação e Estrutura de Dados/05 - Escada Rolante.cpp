#include <iostream>

using namespace std;
 
int main() {
 
    int n, k1;
    int k2 = -10;

    int t = 0;
    int temp;
    
    scanf(" %d", &n);

    for (int i = 0; i < n; i++) {
        scanf(" %d", &k1);
        t += 10;

        temp = k1 - k2;

        if(temp < 10){
            t -= 10 - temp;
        }

        k2 = k1;
    }

    printf("%d\n", t);
    return 0;
}