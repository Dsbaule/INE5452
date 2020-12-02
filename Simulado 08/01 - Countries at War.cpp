#include<bits/stdc++.h> 
using namespace std; 
  
#define DEFAULT_TIME 10000

// Solves the all-pairs shortest path  
// problem using Floyd Warshall algorithm  
void floydWarshall (int dist[][500], int N)  
{
    int i, j, k;

    for (k = 0; k < N; k++)  
    {  
        // Pick all vertices as source one by one  
        for (i = 0; i < N; i++)  
        {  
            // Pick all vertices as destination for the  
            // above picked source  
            for (j = 0; j < N; j++)  
            {  
                // If vertex k is on the shortest path from  
                // i to j, then update the value of dist[i][j]  
                if (dist[i][k] + dist[k][j] < dist[i][j])  
                    dist[i][j] = dist[i][k] + dist[k][j];  
            }  
        }  
    }
} 

int main(){
    int N, E, X, Y, H, K;
    int delivery_time[500][500];
    

    while(cin >> N >> E){
        if((N == 0) && (E == 0))
            return 0;
        // Set matrix to MAX_INT
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                delivery_time[i][j] = DEFAULT_TIME;
        
        // Read input times
        while(E--){
            cin >> X >> Y >> H;
            X--; Y--;
            if (delivery_time[Y][X] < DEFAULT_TIME) {
                delivery_time[Y][X] = 0;
                delivery_time[X][Y] = 0;
            } else {
                delivery_time[X][Y] = H;
            }
        }

        // Calculate optimal delivery times
        floydWarshall(delivery_time, N);

        // Get number of queries
        cin >> K;

        while(K--){
            cin >> X >> Y;
            X--; Y--;
            if(delivery_time[X][Y] == DEFAULT_TIME)
                cout << "Nao e possivel entregar a carta" << endl;
            else
                cout << delivery_time[X][Y] << endl;
        }

        cout << endl;
    }
}