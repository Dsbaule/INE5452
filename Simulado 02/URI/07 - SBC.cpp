using namespace std;

#include <stdio.h>

int main(){
    int n, t, c;
    int processes[100000][2];

    scanf("%d ", &n);

    for(int i = 0; i < n; i++){
        scanf("%d %d", &t, &c);
        processes[i][0] = t;
        processes[i][1] = c;
    }

    int total = 0;
    int cur_time = 1;

    
}