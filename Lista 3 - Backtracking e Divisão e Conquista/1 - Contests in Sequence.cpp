#include <iostream>
#include <set>

using namespace std;

int main() {
    int N, M;
    int values[3];

    while(cin >> N >> M){

        for(int i = 0; i < N; i++)
            cin >> values[i];
        
        set<int> pontuacoes_possiveis;
        pontuacoes_possiveis.clear();
		bool repetido = false;

        int pontuacao;

        int contest[3];
		
        // Sim, poderia ser uma função recursiva, mas no final de contas seria a mesma coisa
        if(N > 1) {
            for(contest[0] = 0; (contest[0] < M) && (!repetido); contest[0]++) {
                for(contest[1] = 0; (contest[1] < M) && (!repetido); contest[1]++) {
                    for(contest[2] = 0; (contest[2] < M) && (!repetido); contest[2]++) {
                        pontuacao = 0;
                        for(int c = 0; c < N; c++)
                            pontuacao += contest[c] * values[c];
                        
                        repetido |= pontuacoes_possiveis.find(pontuacao) != pontuacoes_possiveis.end();
                        pontuacoes_possiveis.insert(pontuacao);

                        if(repetido || (N < 3))
                            break;
                    }
                }
            }
        }

        if(repetido)
            cout << "Try again later, Denis..." << endl;
        else
            cout << "Lucky Denis!" << endl;		
    }
}