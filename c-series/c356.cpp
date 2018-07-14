#include <cstdio>
#include <iostream>
using namespace std;
int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    char c;
    unsigned short n, count = 0;
    cin >> n;
    while ((c = getchar()) != '\n') {
        if (count == 0) {
            cout << c;
        } else if (count == n) {
            count = -1;
        }
        count++;
    }
    cout << '\n';
}