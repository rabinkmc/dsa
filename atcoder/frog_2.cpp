#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    vector<int> stones;

    for (int i = 0 ; i < n; i++) {
        int val;
        cin >> val;
        stones.push_back(val);
    }
    vector<int> dp(n);
    dp[0] = 0 ;
    for (int i = 1; i < n; i++) {
        dp[i] = INT_MAX;
        for (int j=i-1; j >= i-k && j >= 0; j--) {
            int d1 = abs(stones[i] - stones[j]);
            dp[i] = min(dp[i], dp[j] + d1);
        }
    }
    cout << dp[n-1] << "\n";
    return 0;
}
