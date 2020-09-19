#include <iostream>

using namespace std;

int getAndUpdateSmallest(int bancos[][2], int b1) {
    if (bancos[b1][0] == b1)
        return b1;
    else {
        int b2 = getAndUpdateSmallest(bancos, bancos[b1][0]);
        bancos[b1][0] = b2;
        return b2;
    }
}

int getAndUpdateLargest(int bancos[][2], int b1) {
    if (bancos[b1][1] == b1)
        return b1;
    else {
        int b2 = getAndUpdateLargest(bancos, bancos[b1][1]);
        bancos[b1][1] = b2;
        return b2;
    }
}

int main() {
    int n, b;
    int bancos[100000][2];

    scanf(" %d %d", &n, &b);

    for(int i = 0; i < n; i++) {
        bancos[i][0] = i;
        bancos[i][1] = i;
    }

    char c;
    int b1, b2;

    for(int i = 0; i < b; i++) {
        scanf(" %c %d %d", &c, &b1, &b2);

        b1--;
        b2--;

        if (c == 'F') {
            if (getAndUpdateSmallest(bancos, b1) >= getAndUpdateSmallest(bancos, b2)) {
                bancos[bancos[b1][0]][0] = bancos[b2][0];
                bancos[b1][0] = bancos[b2][0];
            }else{
                bancos[bancos[b2][0]][0] = bancos[b1][0];
                bancos[b2][0] = bancos[b1][0];
            }
            if (getAndUpdateLargest(bancos, b1) <= getAndUpdateLargest(bancos, b2)) {
                bancos[bancos[b1][1]][1] = bancos[b2][1];
                bancos[b1][1] = bancos[b2][1];
            }else{
                bancos[bancos[b2][1]][1] = bancos[b1][1];
                bancos[b2][1] = bancos[b1][1];
            }
        } else if ((getAndUpdateSmallest(bancos, b1) == getAndUpdateSmallest(bancos, b2)) || (getAndUpdateLargest(bancos, b1) == getAndUpdateLargest(bancos, b2))) {
            printf("S\n");
        } else {
            printf("N\n");
        }
        /*
        for(int j = 0; j < n; j++) {
            printf("%d: %d\n", j + 1, bancos[j] + 1);
        }
        */
    }
    printf("\n");
    return 0;
}