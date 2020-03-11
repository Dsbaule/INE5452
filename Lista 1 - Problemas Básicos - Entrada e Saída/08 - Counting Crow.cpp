#include <iostream>
 
using namespace std;
 
int main() {
 
    string line;

    int result = 0;
    int i = 0;
    while(i < 3){
        getline(cin, line);
        
        if(line[0] == 'c'){
            printf("%d\n", result);
            result = 0;
            i++;
            continue;
        }
        
        if(line[0] == '*')
            result += 4;
        if(line[1] == '*')
            result += 2;
        if(line[2] == '*')
            result += 1;
    }
 
    return 0;
}