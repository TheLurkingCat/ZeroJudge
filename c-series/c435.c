#include <stdio.h>

#define max(X, Y) (X) > (Y) ? (X) : (Y)
#define min(X, Y) (X) < (Y) ? (X) : (Y)

int main() {
    int arr[100000], i, n, min_value, ans;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    min_value = arr[n - 1];
    ans = arr[n - 2] - arr[n - 1];

    for (i = n - 2; i > -1; i--) {
        ans = max(ans, arr[i] - min_value);
        min_value = min(min_value, arr[i]);
    }

    printf("%d\n", ans);
    return 0;
}