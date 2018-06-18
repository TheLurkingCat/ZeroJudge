#include <algorithm>
#include <iostream>

using namespace std;
int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n, m, i, j;
    while (cin >> n >> m) {
        char s[21] = {'\0'};
        for (i = 0; i < n; i++) {
            s[i] = 'S';
        }
        for (j = i; j < i + m; j++) {
            s[j] = 'L';
        }
        do {
            cout << s << '\n';
        } while (prev_permutation(s, s + m + n));
        cout << '\n';
    }
}