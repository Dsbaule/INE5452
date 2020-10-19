#include <iostream>
#include <bits/stdc++.h>

using namespace std;


double calcArea(int paperStrips[10000], int n, double height)
{
	double ans = 0.0;

	for (int i = n - 1; i >= 0; i--)
	{
		if (height >=  (double)paperStrips[i])
            return ans;
		
		ans += (double)paperStrips[i] - height;
	}

	return ans;
}

double findHeight(int paperStrips[10000], int n, int a) {
    sort(paperStrips, paperStrips + n);

	double low = 0.0;
	double high = (double)paperStrips[n - 1];
	double mid;
	
	while (low <= high)
	{
		mid = (low + high) / 2.0;

		double area = calcArea(paperStrips, n, mid);
		if (fabs(area - (double)a) < 1e-4) 
            return mid;
		
		if (area < a)
            high = mid;
		else 
            low = mid;
	}

	return -1;
}

int main()
{
    int n, a;
    int paperStrips[10000];

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
