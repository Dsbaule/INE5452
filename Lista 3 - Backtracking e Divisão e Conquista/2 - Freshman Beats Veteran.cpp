#include <iostream>

using namespace std;

int main() {
    int N,  cur_number, i, index, total;
    string inputString;

    while(cin >> N ){
        int numbers[N];
        total = 0;

        for(i = 0; i < N; i++)
            numbers[i] = 0;

        for(i = 0; i < N; i++) {
            cin >> inputString;
            
            for(index = 0; (inputString[index] != '/') && (index < 10); index++);
            cur_number = stoi(inputString.substr(0, index));
            //cout << cur_number << endl;
            
            for(int j = 0; j < i; j++)
                if(numbers[j] > cur_number)
                    total++;

            numbers[i] = cur_number;            
        }

        cout << total << endl;
    }

}