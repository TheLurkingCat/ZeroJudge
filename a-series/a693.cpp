#include <iostream>

using namespace std;

int food[100000];

int main(void) {
    food[0] = 0;
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int a, b, n, m, temp;
    while (cin >> n >> m) {
        n++;
        for (int i = 1; i < n; i++) {
            cin >> temp;
            food[i] = food[i - 1] + temp;
        }
        for (int i = 0; i < m; i++) {
            cin >> a >> b;
            cout << food[b] - food[a - 1] << '\n';
        }
    }
}
