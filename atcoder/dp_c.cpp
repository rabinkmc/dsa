#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int arr[n][3];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> arr[i][j];
        }
    }
    int dp[n][3];
    for (int j=0; j < 3; j++) {
        dp[0][j] = arr[0][j];
    }
    for (int i =1 ; i < n; i++) {
        for (int j =0 ; j < 3; j++) {
            int col1, col2;
            if (j == 0) {
                col1 = 1;
                col2 = 2;
            }
            if (j == 1 ) {
                col1 = 0;
                col2 = 2;
            }
            if (j == 2 ) {
                col1 = 0;
                col2 = 1;
            }
            int prev_max = max(dp[i-1][col1], dp[i-1][col2]);
            dp[i][j] = arr[i][j] + prev_max;
        }
    }
    int ans = max(dp[n-1][0], dp[n-1][1]);
    ans = max(ans, dp[n-1][2]);
    cout << ans << "\n";
}
