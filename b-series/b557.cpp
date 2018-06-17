#include <iostream>
#include <vector>

using namespace std;

bool isAnswer(int a, int b, int c) {
    if (a * a + b * b == c * c) {
        return true;
    }
    return false;
}

int main(void) {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    unsigned int T, N, number, answer;
    int list[102], smallNumber, middleNumber, bigNumber;
    vector<int> useNumberList;
    unsigned long vSize;

    while (cin >> T) {
        for (int iT = 0; iT < T; iT++) {
            cin >> N;
            for (int i = 1; i <= 100; i++) {
                list[i] = 0;
            }
            for (int iN = 0; iN < N; iN++) {
                cin >> number;
                list[number]++;
            }
            useNumberList.clear();
            for (int i = 1; i <= 100; i++) {
                if (list[i] > 0) {
                    useNumberList.push_back(i);
                }
            }
            vSize = useNumberList.size();
            answer = 0;
            for (int i = 0; i < vSize - 2; i++) {
                for (int j = i + 1; j < vSize - 1; j++) {
                    for (int k = j + 1; k < vSize; k++) {
                        smallNumber = useNumberList[i];
                        middleNumber = useNumberList[j];
                        bigNumber = useNumberList[k];
                        if (isAnswer(smallNumber, middleNumber, bigNumber)) {
                            answer = answer + (list[smallNumber] * list[middleNumber] * list[bigNumber]);
                        }
                    }
                }
            }
            cout << answer << '\n';
        }
    }
    return 0;
}