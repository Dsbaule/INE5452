#include <iostream>

using namespace std;

int getAndUpdate(int bancos[], int b1) {
    if (bancos[b1] == b1)
        return b1;
    else {
        bancos[b1] = getAndUpdate(bancos, bancos[b1]);
        return bancos[b1];
    }
}

int main() {
    int n, b;
    int bancos[100000];

    scanf(" %d %d", &n, &b);

    for(int i = 0; i < n; i++) {
        bancos[i] = i;
    }

    char c;
    int b1, b2;

    for(int i = 0; i < b; i++) {
        scanf(" %c %d %d", &c, &b1, &b2);

        b1--;
        b2--;

        if (c == 'F') {
            if (getAndUpdate(bancos, b1) >= getAndUpdate(bancos, b2)) {
                bancos[bancos[b1]] = bancos[b2];
            }else{
                bancos[bancos[b2]] = bancos[b1];
            }
        } else if (getAndUpdate(bancos, b1) == getAndUpdate(bancos, b2)) {
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
    return 0;
}