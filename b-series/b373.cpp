#include <iostream>
using namespace std;

int main() {
    int n, train[10000];
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    while (cin >> n) {
        int cnt = 0;

        for (int i = 0; i < n; ++i)
            cin >> train[i];

        for (int i = 0; i < n - 1; ++i)
            for (int j = 0; j < n - i - 1; ++j)
                if (train[j] > train[j + 1]) {
                    train[j] ^= train[j + 1] ^= train[j] ^= train[j + 1];
                    cnt++;
                }

        cout << cnt << '\n';
    }
    return 0;
}