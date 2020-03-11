#include <iostream>
 
using namespace std;
 
int main() {
 
    int numGames;
    scanf("%d", &numGames);
    getchar();

    char winner;

    int winsA = 0, winsD = 0;
    for(int i = 0; i < numGames; i++) {
        if(getchar() == 'A')
            winsA++;
        else
            winsD++;
    }
    if(winsA > winsD)
        printf("Anton\n");
    else if(winsA < winsD)
        printf("Danik\n");
    else
        printf("Friendship\n");

    return 0;
}