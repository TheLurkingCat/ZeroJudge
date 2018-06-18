#include <iostream>
#include <sstream>

using namespace std;

bool isAllDigit(string str);

int main(int argc, char** argv) {
    string input;

    while (getline(cin, input)) {
        int sum = 0;
        istringstream iString(input);
        while (iString) {
            string word;
            iString >> word;
            if (isAllDigit(word)) {
                sum += atoi(word.c_str());
            }
        }
        cout << sum << '\n';
    }
}

bool isAllDigit(string str) {
    for (int i = 0; i < str.length(); i++) {
        if (!isdigit(str[i]))
            return false;
    }
    return true;
}
