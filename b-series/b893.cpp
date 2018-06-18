#include <cmath>
#include <iostream>

using namespace std;
int s[6];
int f(int x) {
    long long c = s[0] * pow(x, 5) + s[1] * pow(x, 4) + s[2] * pow(x, 3) + s[3] * pow(x, 2) + s[4] * x + s[5];
    if (s[0] == 0 && s[1] == 0 && s[2] == 0 && s[3] == 0 && s[4] == 0 && s[5] == 0) {
        return 2;
    } else {
        if (c > 0) {
            return 1;
        } else if (c == 0) {
            return 0;
        } else {
            return -1;
        }
    }
}
int main() {
    while (cin >> s[0] >> s[1] >> s[2] >> s[3] >> s[4] >> s[5]) {
        int min = -75;
        int a, b;
        bool flag = false;
        while (min < 75) {
            a = f(min);
            b = f(min + 1);
            if (a == 0) {
                cout << min << " " << min << endl;
                flag = true;
            } else if (a == 2) {
                cout << "Too many... = =\"" << endl;
                flag = true;
                break;
            } else if (a * b < 0) {
                cout << min << " " << min + 1 << endl;
                flag = true;
            }
            min++;
        }
        if (!flag) cout << "N0THING! >\\\\\\<" << endl;
    }
    return 0;
}
