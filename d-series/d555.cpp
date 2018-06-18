#include <memory.h>
#include <algorithm>
#include <iostream>

using namespace std;
struct point {
    int x, y;
} p[500000], k;
int ox[500000];
bool cmp(point a, point b) {
    return a.y > b.y || (a.y == b.y) && (a.x > b.x);
}
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n, t, i, j;
    for (t = 1; cin >> n; t++) {
        for (i = 0; i < n; i++) cin >> p[i].x >> p[i].y;
        sort(p, p + n, cmp);
        memset(ox, 0, sizeof(ox));
        k.x = -1;
        k.y = 1000000;
        j = 0;
        for (i = 0; i < n; i++) {
            if (k.y != p[i].y && k.x < p[i].x) {
                ox[j] = i;
                j++;
                k = p[i];
            }
        }
        cout << "Case " << t << ":\nDominate Point: " << j << '\n';
        for (i = 0; i < j; i++) cout << "(" << p[ox[i]].x << "," << p[ox[i]].y << ")\n";
    }
}