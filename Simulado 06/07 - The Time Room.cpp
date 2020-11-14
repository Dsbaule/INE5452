#include <iostream>

using namespace std;

int main(){
    long long x, y, ans;
	int cases;
	
	cin >> cases;
	while(cases--)
	{
		cin >> x >> y;
		
		if (y > x) 
			cout << "2" << endl;
		else if((x % y) == 0)
            cout << x/y << endl;
        else
            cout << x/y + 1 << endl;
	}
}