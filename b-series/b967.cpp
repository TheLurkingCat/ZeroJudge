#include <deque>
#include <iostream>

using namespace std;
deque<int> F[100001];

int md;

int DFS(int x) {
    int max_1, max_2, result, k = F[x].size(), i;
    if (k == 0) {
        return 0;
    } else if (k == 1) {
        return DFS(F[x][0]) + 1;
    } else {
        for (i = 0; i < k; i++) {
            result = DFS(F[x][i]) + 1;
            if (i == 0) {
                max_1 = result;
            } else if (i == 1) {
                if (max_1 >= result) {
                    max_2 = result;
                } else {
                    max_2 = max_1;
                    max_1 = result;
                }
            } else {
                if (max_1 <= result) {
                    max_2 = max_1;
                    max_1 = result;
                } else if (max_2 < result) {
                    max_2 = result;
                }
            }
        }
        md = max(md, max_1 + max_2);
        return max_1;
    }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int a, b, root, n, i;
    bool is_child[100001];
    while (cin >> n) {
        md = 0;
        for (i = 0; i < n; i++) {
            F[i].clear();
            is_child[i] = false;
        }
        for (i = 1; i < n; i++) {
            cin >> a >> b;
            F[a].push_back(b);
            is_child[b] = true;
        }
        for (i = 0; i < n; i++) {
            if (!is_child[i]) {
                root = i;
                break;
            }
        }
        cout << max(DFS(root), md) << '\n';
    }
}