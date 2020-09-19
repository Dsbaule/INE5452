#include <iostream>

using namespace std;

void swap(int input_list[], int index1, int index2) {
    int temp = input_list[index1];
    input_list[index1] = input_list[index2];
    input_list[index2] = temp;
}

int sort_train(int train[], int l) {
    int swaps = 0;
    bool something_changed;

    do {

        something_changed = false;

        for(int j = 0; j < (l - 1); j++){
            if(train[j] > train[j+1]){
                something_changed = true;
                swap(train, j, j+1);
                swaps++;
            }
        }

    } while(something_changed);

    return  swaps;
}

int main() {
    int n, l;
    int train[50];
    int swaps;

    scanf(" %d", &n);

    for(int i = 0; i < n; i++){
        scanf(" %d", &l);
        
        for(int j = 0; j < l; j++){
            scanf(" %d", &train[j]);
        }
        
        swaps = sort_train(train, l);
        printf("Optimal train swapping takes %d swaps.\n", swaps);
    }


    return 0;
}