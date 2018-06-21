#include <string.h>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    char s[1024];
    while (cin >> s) {
        int A[1024] = {}, m, n = 0;
        if (!(cin >> s)) {
            return 0;
        }
        m = strlen(s);
        reverse(s, s + m);
        for (int i = 0; i < m; i++)
            A[i] += s[i] - 'A';
        n = max(n, m);

        if (!(cin >> s)) {
            return 0;
        }
        m = strlen(s);
        reverse(s, s + m);
        for (int i = 0; i < m; i++)
            A[i] += s[i] - 'A';
        n = max(n, m);

        for (int i = 0; i < n; i++) {
            if (A[i] >= 26) {
                A[i + 1] += A[i] / 26;
                A[i] %= 26;
                n = max(n, i + 2);
            }
        }

        for (int i = n - 1; i >= 0; i--)
            cout << (char)(A[i] + 'A');
        cout << '\n';
    }
    return 0;
}