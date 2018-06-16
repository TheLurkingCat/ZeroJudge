#include <iostream>
#include <set>
#include <string>
using namespace std;

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    string n, m;
    set<string> acs;
    set<string> other;
    struct data_type {
        string name;
        string state;
    };
    int a, c = 0;
    cin >> a;
    data_type submission[a];
    for (int i = a - 1; i > -1; i--) {
        cin >> n >> m;
        submission[i].name = n;
        submission[i].state = m;
    }
    for (int i = 0; i < a; i++) {
        if (submission[i].state != "AC") {
            other.insert(submission[i].name);
            continue;
        }
        if (acs.count(submission[i].name)) {
            continue;
        }
        acs.insert(submission[i].name);
        if (!other.count(submission[i].name)) {
            c++;
        }
    }
    cout << c * 100 / acs.size() << "%\n";
}