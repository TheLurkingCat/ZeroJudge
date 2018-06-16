#include <iostream>

using namespace std;

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n;
    while (cin >> n) {
        if (n & 1) {
            cout << n - 1 << '\n';
        } else {
            cout << n << '\n';
        }
    }
    return 0;
}