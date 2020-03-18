#include <iostream>
 
using namespace std;
 
int main() {
 
    int N , Q, total;
    const int maxMarbleValue = 10000;
    int count[maxMarbleValue + 1];
    int sum[maxMarbleValue + 1];
    int currentNumber, query;
    int currentCase = 1;

    scanf (" %d %d", &N , &Q );

    while((N != 0) || (Q != 0)) {
    	for(int i = 0; i <= maxMarbleValue; i++) {
    		count[i] = 0;
    	}

    	for(int i = 0; i < N; i++) {
    		scanf (" %d", &currentNumber);
    		count[currentNumber]++;
    	}

        sum[0] = 0;
        for (int i = 1; i <= maxMarbleValue; i++) {
            sum[i] = sum[i - 1] + count[i - 1];
        }

        printf ("CASE# %d:\n", currentCase);
    	for(int i = 0; i < Q; i++) {
    		scanf (" %d", &query);
    		if(count[query] == 0){
    			printf ("%d not found\n", query);
            } else {
    			printf ("%d found at %d\n", query, sum[query] + 1);
            }
    	}

    	currentCase++;
    	scanf (" %d %d", &N , &Q );
    }
    
    return 0;
}