#include <cmath>
#include <iostream>

using namespace std;

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    long long a, b, i, x;
    double target;
    while (cin >> a >> b) {
        x = (a / 2) < b ? (a - b) : b;
        target = 0;
        for (i = 0; i < x; i++) {
            target += log10(a - i) - log10(x - i);
        }
        cout << (int)target + 1 << '\n';
    }
    return 0;
}
