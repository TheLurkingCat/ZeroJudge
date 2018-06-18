#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int> > V;
vector<int> X;
multiset<int> S;

int main(void) {
    int n, m, l, r, ret = 0;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> l >> r;
        V.push_back(make_pair(l, r));
        X.push_back(l - 1);
        X.push_back(l);
        X.push_back(r);
        X.push_back(r + 1);
    }

    sort(X.begin(), X.end());
    sort(V.begin(), V.end());
    X.resize(unique(X.begin(), X.end()) - X.begin());

    for (int i = 1, pos = 0; i < X.size(); i++) {
        int x = X[i];
        while (!S.empty() && *S.begin() <= X[i - 1])
            S.erase(S.begin());
        while (pos < m && V[pos].first == x)
            S.insert(V[pos].second), pos++;
        if (S.size() % 2)
            ret += X[i] - X[i - 1];
    }

    cout << n - ret << '\n';

    return 0;
}