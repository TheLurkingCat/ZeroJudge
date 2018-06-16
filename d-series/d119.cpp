#include <iostream>
#include <sstream>

using namespace std;

unsigned long long int result[10][50001] = {};

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int coin[10] = {1, 5, 10, 20, 50, 100, 200, 500, 1000, 2000}, num, sum;
    string s;
    for (int i = 0; i <= 50000; i++) result[0][i] = 1;
    for (int i = 0; i < 10; i++) result[i][0] = 1;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < coin[i]; j++) {
            result[i][j] = result[i - 1][j];
        }
        for (int j = coin[i]; j < 50001; j++) {
            result[i][j] = result[i - 1][j] + result[i][j - coin[i]];
        }
    }
    while (getline(cin, s)) {
        istringstream read(s);
        sum = 0;
        while (read >> num) {
            sum += num;
        }
        if (sum != 0)
            cout << result[9][sum] - 1 << '\n';
    }
}
