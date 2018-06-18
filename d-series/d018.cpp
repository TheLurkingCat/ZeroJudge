#include <iostream>
#include <sstream>
#include <string>

using namespace std;
int main() {
    string str;
    while (getline(cin, str)) {
        istringstream instr(str);
        double sum = 0;
        while (instr >> str) {
            int pos = str.find(':', 0);
            int num = atoi(str.substr(0, pos).c_str());
            double num2 = atof(str.substr(pos + 1, str.length()).c_str());
            num& 1 ? sum += num2 : sum -= num2;
        }
        cout << sum << endl;
    }
    return 0;
}
