#include <iostream>
 
using namespace std;
 
int main() {
 
    int N, J, M, current;
    scanf ("%d", &N);

    while(N != 0) {
    	M = 0;
    	J = 0;

    	for(int i = 0; i < N; i++){
    		scanf(" %d", &current);
    		if(current == 0)
    			M++;
    		else
    			J++;
    	}

    	printf ("Mary won %d times and John won %d times\n", M, J);
    	scanf ("%d", &N);
    }
    return 0;
}