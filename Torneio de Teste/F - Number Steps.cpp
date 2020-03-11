#include <iostream>
 
using namespace std;
 
int main() {

    int numCases;
    scanf("%d", &numCases);
    
    int x, y;

    for(int i = 0; i < numCases; i++){
        scanf("%d %d", &x, &y);

        if(x == y){
            if((y % 2) == 0)
                printf("%d\n", y * 2);
            else
                printf("%d\n", (y * 2) - 1);
        }else if(x == (y + 2)){
            if((y % 2) == 0)
                printf("%d\n", (y * 2) + 2);
            else
                printf("%d\n", (y * 2) + 1);
        }else {
            printf("No Number\n");
        }


    }

    return 0;
}