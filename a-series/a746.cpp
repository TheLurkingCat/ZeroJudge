#include <memory.h>
#include <iostream>

using namespace std;

int main() {
    int A, B;
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    while (cin >> A >> B) {
        char Fence[A + 2][A + 2];
        memset(Fence, ' ', sizeof(char) * (A + 2) * (A + 2));
        for (int i = 0; i <= A + 1; i = i + (A + 1))
            for (int j = 0; j <= A + 1; j++) {
                Fence[i][j] = '-';
                Fence[j + 1][i] = '|';
            }
        int x1, y1, x2, y2;
        for (int i = 1; i <= B; i++) {
            cin >> x1 >> y1;
            if (i == 1) {
                Fence[x1][y1] = '*';
            } else if (x2 == x1) {
                if (y1 > y2) {
                    for (int i = y2; i <= y1; i++)
                        Fence[x1][i] = '*';
                } else {
                    for (int i = y2; i >= y1; i--)
                        Fence[x1][i] = '*';
                }
            } else if (y2 == y1) {
                if (x1 > x2) {
                    for (int i = x2; i <= x1; i++)
                        Fence[i][y2] = '*';
                } else {
                    for (int i = x2; i >= x1; i--)
                        Fence[i][y2] = '*';
                }
            }
            x2 = x1;
            y2 = y1;
        }
        for (int i = 0; i <= A + 1; i++) {
            for (int j = 0; j <= A + 1; j++) {
                cout << Fence[i][j];
            }
            cout << '\n';
        }
    }
}