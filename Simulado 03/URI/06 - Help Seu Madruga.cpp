#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int n, a;
int paperStrips[10000];

double findHeight(int paperStrips[10000], int n, int a) {
    sort(paperStrips, paperStrips + n);
    
    int totalArea = 0;
    int i;
    for (i = n - 1; i > 0; i--) {
        if ((a - totalArea) < ((n - i) * (paperStrips[i] - paperStrips[i - 1])))
            break;
        totalArea += (paperStrips[i] - paperStrips[i - 1]) * (n - i);
    }
    double leftOverHeight = ((double)(a - totalArea))/((double)(n - i));
    double height = ((double)paperStrips[i]) - leftOverHeight;
    return height;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while(true){
        cin >> n >> a;

        if ((n == 0) and (a == 0))
            break;

        int totalArea = 0;

        for (int i = 0; i < n; i++)
        {
            cin >> paperStrips[i];
            totalArea += paperStrips[i];
        }

        if (a > totalArea){
            cout << "-.-" << endl;
        } else if (a == totalArea) {
            cout << ":D" << endl;
        } else {
            printf("%.4f\n", findHeight(paperStrips, n, a));
        }
    }

    return 0;
}
