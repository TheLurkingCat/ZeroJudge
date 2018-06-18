#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;
typedef long long LL;
int main(void) {
    LL a[3];
    while (cin >> a[0] >> a[1] >> a[2]) {
        int p[3] = {0, 1, 2};
        for (int i = 0; i < 3; i++) {
            if (a[p[1]] + a[p[2]] < a[p[0]] ||
                (a[p[0]] + a[p[1]] > a[p[2]] && a[p[2]] > a[p[0]] && a[p[0]] > a[p[1]]) ||
                (a[p[0]] + a[p[2]] > a[p[1]] && a[p[1]] > a[p[0]] && a[p[0]] > a[p[2]])) {
                printf("%c\n", i + 65);
                break;
            }
            swap(p[0], p[i + 1]);
        }
    }
}
