#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int main(void) {
    int x1, y1, x2, y2, a, b, c, d;

    while (cin >> x1 >> y1 >> x2 >> y2) {
        int xtemp = pow((double)(x2 - x1), 2);
        int ytemp = y2 - y1;
        int gcdtemp = __gcd((xtemp), (ytemp));
        xtemp /= gcdtemp;
        ytemp /= gcdtemp;

        a = xtemp, b = ytemp, c = -2 * ytemp * x1, d = ytemp * pow((double)x1, 2) + y1 * xtemp;
        cout << a << "y = " << b << "x^2 + " << c << "x + " << d << '\n';
    }
}