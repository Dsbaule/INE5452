using namespace std;

#include <iostream>
#include <queue>
#include <vector>

class Process {
    public:
        long long int t;
        long int c;
    
    Process(long int t, int c){
        this->t = t;
        this->c = c;
    }
};

class Compare_c {
public:
    bool operator () (const Process* p1, const Process* p2) {
        return (p1->c > p2->c);
    }
};

class Compare_t {
public:
    bool operator () (const Process* p1, const Process* p2) {
        return (p1->t > p2->t);
    }
};

int main(){
    long int n, t, c;
    Process *process, *cur_process;
    long long int total, cur_time;

    priority_queue<Process*, vector<Process*>, Compare_t> process_list;
    priority_queue<Process*, vector<Process*>, Compare_c> process_queue;

    while(cin >> n){
        total = 0;
        cur_time = 1;

        for(long int i = 0; i < n; i++){
            cin >> t >> c;
            process = new Process(t, c);
            process_list.push(process);
        }

        while (!(process_queue.empty() && process_list.empty())) {
            //cout << process_list.empty() << process_queue.empty() << endl;
            if (process_queue.empty() && (process_list.top()->t > cur_time)) {
                cur_time = process_list.top()->t;
            }

            while ((!process_list.empty()) && (process_list.top()->t <= cur_time)) {
                cur_process = process_list.top();
                process_queue.push(cur_process);
                process_list.pop();
            }

            cur_process = process_queue.top();
            total += cur_time - cur_process->t;
            cur_time += cur_process->c;
            process_queue.pop();
        }

        cout << total << endl;
    }

    
}