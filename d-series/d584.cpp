#include <iostream>

using namespace std;

int main(void) {
    int n, m, point;
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    while (cin >> n >> m) {
        if (n == 0) {
            cout << "0\n";
        } else if (n == 2) {
            if (m < 8) {
                cout << "0\n";
            } else {
                point = 1 + 3 * (m - 8);
                if (m > 29) point++;
                if (m > 69) point++;
                if (m > 119) point += 3;
                cout << point << '\n';
            }
        } else {
            if (m < 10) {
                cout << "0\n";
            } else {
                point = 1 + 3 * (m - 10);
                if (m > 29) point++;
                if (m > 69) point++;
                if (m > 119) point += 3;
                cout << point << '\n';
            }
        }
    }
    return 0;
}