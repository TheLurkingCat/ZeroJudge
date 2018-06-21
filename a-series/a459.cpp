#include <string.h>
#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    char str[100];
    int top = 0, brain[240] = {}, record[1000] = {};
    while (cin >> str) {
        if (!strcmp(str, "(>OwO)>u~(/OwO)/nya~"))
            record[top] = 0;
        if (!strcmp(str, "(>OwO)>u~!(/OwO)/nya~!"))
            record[top] = 1;
        if (!strcmp(str, "(>OwO)>u~!!(/OwO)/nya~!!"))
            record[top] = 2;
        if (!strcmp(str, "(>OwO)>u~!!!(/OwO)/nya~!!!"))
            record[top] = 3;
        if (!strcmp(str, "CHAOS")) {
            cin >> str;
            record[top] = 4;
        }
        if (!strcmp(str, "I")) {
            cin >> str >> str;
            record[top] = 5;
        }
        if (!strcmp(str, "Let's\\(OwO)/nya~"))
            record[top] = 6;
        top++;
    }
    int index = 0;
    for (int i = 0; i < top; i++) {
        switch (record[i]) {
            case 0:
                index++;
                break;
            case 1:
                brain[index]++;
                break;
            case 2:
                index--;
                break;
            case 3:
                brain[index]--;
                break;
            case 4:
                if (brain[index] == 0) {
                    int cnt = 0;
                    while (cnt >= 0) {
                        i++;
                        if (record[i] == 4)
                            cnt++;
                        if (record[i] == 5)
                            cnt--;
                    }
                }
                break;
            case 5:
                if (brain[index]) {
                    int cnt = 0;
                    i--;
                    while (cnt >= 0) {
                        if (record[i] == 4)
                            cnt--;
                        if (record[i] == 5)
                            cnt++;
                        i--;
                    }
                }
                break;
            case 6:
                cout << (char)(brain[index]);
                break;
        }
    }
    cout << '\n';
    return 0;
}