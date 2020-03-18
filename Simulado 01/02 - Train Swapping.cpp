#include <iostream>
 
using namespace std;

void swap(int index1, int index2, int * array){
	int temp = array[index1];
	array[index1] = array[index2];
	array[index2] = temp;
}

int main() {
 
    int N , L, currentNumber, numberOfSwaps;
    int train[50];

    scanf ("%d\n", &N);

    for (int i = 0; i < N; i++) {
    	scanf (" %d", &L);

    	for (int j = 0; j < L; j++){
    		scanf(" %d", &train[j]);
    	}

    	numberOfSwaps = 0;

    	for(int i = 0; i < L - 1; i++) {
    		for(int j = 0; j < L - i - 1; j++) {
    			if (train[j] > train[j + 1]) {
    				numberOfSwaps++;
    				swap(j, j + 1, train);
    			}
    		}
    	}

    	printf("Optimal train swapping takes %d swaps.\n", numberOfSwaps);
    }
    return 0;
}