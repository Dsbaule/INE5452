#include <iostream>
 
using namespace std;
 
int main() {
 
    char alphabet[27];

    while(scanf("%s", alphabet) != EOF) {
        int length;
        scanf("%d", &length);
        
        int letters[length];
        for(int i = 0; i < length; i++)
            scanf("%d", &letters[i]);

        for(int i = 0; i < length; i++)
            printf("%c", alphabet[letters[i] - 1]);
        printf("\n");
    }
    return 0;
}