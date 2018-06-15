#include <algorithm>
#include <iostream>

using namespace std;

int c[30];
int s[30];
int sum;
int flag = 0;

void recursive(int N, int n, int t, int total) {
    int i;

    if (total > t) return;
    if (n == N) {
        sum = 0;

        for (i = 0; i < N; i++)
            if (s[i]) {
                sum += c[i];
            }

        if (sum == t) {
            for (i = 0; i < N; i++)
                if (s[i]) {
                    cout << c[i] << ' ';
                }
            flag = 1;
            cout << '\n';
        }

        return;
    }

    s[n] = 1;
    total += c[n];
    recursive(N, n + 1, t, total);
    total -= c[n];

    s[n] = 0;
    recursive(N, n + 1, t, total);
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int N, t, i, j, temp;
    cin >> N;
    cin >> t;
    for (i = 0; i < N; i++)
        cin >> c[i];
    sort(c, c + N);
    cout << '\n';
    recursive(N, 0, t, 0);
    if (flag == 0) {
        cout << "-1\n";
    }
}