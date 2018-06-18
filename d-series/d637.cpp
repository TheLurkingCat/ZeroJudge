#include <iostream>

using namespace std;
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    short n, i, x, y, m;
    int a[101] = {};
    cin >> n;
    m = n;
    while (n) {
        cin >> x >> y;
        i = 100;
        while (i >= x) {
            if (a[i - x] + y > a[i]) {
                a[i] = a[i - x] + y;
            }
            i--;
        }
        n--;
    }
    cout << a[100] << '\n';
}
