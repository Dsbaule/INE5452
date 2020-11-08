#include <iostream>
 
using namespace std;

int remove_emotes(char ** linhas, int N, char ** emotes, int M) {
    
}
 
int main() {
    while(true){
        int N, M;

        char emotes[100][15];
        char linhas[100][80];

        cin >> N >> M;

        if ((N == 0) && (M == 0))
            return 0;
    
        for(int i = 0; i < N; i++)
            cin >> emotes[i];
    
        for(int i = 0; i < M; i++)
            cin >> linhas[i];
            
        

        return 0;
    }
}