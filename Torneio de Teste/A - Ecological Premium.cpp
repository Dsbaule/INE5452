#include <iostream>
 
using namespace std;
 
int main() {
    int numCases, sizeCase, sizeLand, animalCount, environmentFriendliness, caseTotal;

    scanf("%d", &numCases);

    for(int i = 0; i < numCases; i++){
        scanf("%d", &sizeCase);
        caseTotal = 0;
        for(int j = 0; j < sizeCase; j++) {
            scanf("%d %d %d", &sizeLand, &animalCount, &environmentFriendliness);
            caseTotal += sizeLand * environmentFriendliness;
        }
        printf("%d\n", caseTotal);
    }
}