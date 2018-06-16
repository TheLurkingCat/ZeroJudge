#include <memory.h>
#include <iostream>
using namespace std;

int init[3][3] = {{1, 1, 1}, {1, 2, 2}, {2, 3, 4}};

int now[3][3];
int p[3][3];

void pwd(int N) {
    if (N == 0) {
        memset(now, 0, sizeof(now));
        now[0][0] = now[1][0] = now[2][0] = 1;
        return;
    }
    if (N == 1) {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                now[i][j] = init[i][j];

        return;
    }
    pwd(N / 2);
    memset(p, 0, sizeof(p));
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            for (int k = 0; k < 3; k++) {
                p[i][j] += now[i][k] * now[k][j];
                p[i][j] %= 10007;
            }
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            now[i][j] = p[i][j];
    if (N & 1) {
        memset(p, 0, sizeof(p));
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < 3; k++) {
                    p[i][j] += now[i][k] * init[k][j];
                    p[i][j] %= 10007;
                }
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                now[i][j] = p[i][j];
    }
    return;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int N;
    cin >> N;
    pwd((N - 1) / 3);
    int p = (N - 1) % 3;
    cout << (now[p][0] + now[p][1] + now[p][2]) % 10007 << '\n';
    return 0;
}