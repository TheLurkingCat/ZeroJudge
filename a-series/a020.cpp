#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    int english[26] = {10, 11, 12, 13, 14, 15, 16, 17, 34,
                       18, 19, 20, 21, 22, 35, 23, 24, 25,
                       26, 27, 28, 29, 32, 30, 31, 33};
    while (cin >> s) {
        int x;
        for (int i = 0; i < 26; i++)
            if (s[0] - 'A' == i)
                x = english[i] / 10 + (english[i] % 10) * 9;
        if ((x + (s[1] - '0') * 8 + (s[2] - '0') * 7 + (s[3] - '0') * 6 + (s[4] - '0') * 5 + (s[5] - '0') * 4 + (s[6] - '0') * 3 + (s[7] - '0') * 2 + (s[8] - '0') + (s[9] - '0')) % 10 == 0)
            cout << "real" << endl;
        else
            cout << "fake" << endl;
    }
    return 0;
}