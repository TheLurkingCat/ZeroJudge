#include <cmath>
#include <iostream>

using namespace std;

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    uint64_t x;
    while (cin >> x) {
        if (x == 0)
            cout << 0;
        else
            cout << floor(log2(x)) + 1 << '\n';
    }
}