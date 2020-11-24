#include<bits/stdc++.h> 
using namespace std; 
  
// A utility function to add an edge in an 
// undirected graph. 
void addEdge(vector<int> adj[], int u, int v) 
{ 
    adj[u].push_back(v); 
    adj[v].push_back(u); 
}

bool check_side(int guest, vector<int> adj[], int side[], int value) {
    //cout << "Checking " << guest << " " << value << endl;
    side[guest] = value;
    int new_value = (value + 1) % 2;

    for (auto x : adj[guest]) {
        //cout << "\tX " << x << endl;
        if(side[x] == value){
            return false;
        }
        if(side[x] == -1){
            //cout << "\tCalling " << guest << " " << value << endl;
            if(!check_side(x, adj, side, new_value))
                return false;
        }
    }

    return true;
} 
  
// Driver code 
bool compute_one(int n, int m) 
{ 
    int i;
    int g1, g2;
    vector<int> friendly_relations[101];
    int side[101];

    memset(side, -1, sizeof(int) * n);

    while(m--){
        cin >> g1 >> g2;
        addEdge(friendly_relations, g1 - 1, g2 - 1); 
    }

    while(n--){
        if (side[n] == -1)
            if (!check_side(n, friendly_relations, side, 0))
                return false;
    }

    return true; 
}

int main(){
    int n, m;
    int i = 1;
    while(cin >> n >> m){
        cout << "Instancia " << i << endl;
        if(compute_one(n, m))
            cout << "sim" << endl;
        else
            cout << "nao" << endl;
        cout << endl;
        i++;
    }
}