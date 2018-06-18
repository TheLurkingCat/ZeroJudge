#include <stdint.h>
#include <stdio.h>

uint32_t powmod(uint32_t base, uint32_t exp, uint32_t mod) {
    uint32_t res = 1;
    base %= mod;
    while (exp) {
        if (exp % 2)
            res = res * (uint64_t)base % mod;
        exp /= 2;
        base = base * (uint64_t)base % mod;
    }
    return res;
}

int check(uint32_t n, uint32_t s, uint32_t x) {
    uint32_t r;

    if (x != 1 && x != n - 1) {
        for (r = 1; r < s; ++r) {
            x = (uint64_t)x * x % n;
            if (x == n - 1)
                return 1;
        }
        return 0;
    }
    return 1;
}

int isPrime(uint32_t n) {
    uint32_t d, s;

    switch (n) {
        case 1:
            return 0;
        case 2:
        case 7:
        case 61:
        case 97:
            return 1;
    }

    d = n - 1;
    s = 0;

    while (d % 2 == 0) {
        d /= 2;
        ++s;
    }

    return check(n, s, powmod(2, d, n)) &&
           check(n, s, powmod(7, d, n)) &&
           check(n, s, powmod(61, d, n));
}

int main(void) {
    uint32_t n;
    scanf("%u", &n);
    while (n != 0) {
        puts(isPrime(n) ? "0" : "1");
        scanf("%u", &n);
    }
    return 0;
}
