// AC (12ms, 532KB)
#include <iostream>
#include <regex>

using namespace std;

int main(void) {
    regex reg("[^QA]");
    string str;
    cin >> str;
    str = regex_replace(str, reg, "");
    uint64_t i, ans = 0, len = str.size(), Q_right = count(str.begin(), str.end(), 'Q'), Q_left = 0;
    for (i = 0; i < len; i++) {
        if (str[i] == 'Q') {
            Q_left++;
            Q_right--;
        } else {
            ans += Q_left * Q_right;
        }
    }
    cout << ans << '\n';
    return 0;
}
