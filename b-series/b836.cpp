#include <iostream>

using namespace std;

int main(void) {
    unsigned long long n, m, k = 1, t = 0;
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    while (cin >> n >> m) {
        if (m == 0) {
            cout << "Go Kevin!!\n";
        } else {
            while (k < n) {
                t += k;
                k += m;
            }
            if (k == n) {
                cout << "Go Kevin!!\n";
            } else {
                cout << "No Stop!!\n";
            }
        }
    }
    return 0;
}
