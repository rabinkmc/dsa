#include <bits/stdc++.h>

using namespace std;
// h1 h2 h3 h4 ... hi .... hn-1 hn 
// dp(i) = min(abs(hi - hi_1) + dpi_1, abs(hi - hi_2) + dpi_2)

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> stones;

    for (int i = 0 ; i < n; i++) {
        int val;
        cin >> val;
        stones.push_back(val);
    }
    vector<int> dp(n);
    dp[0] = 0 ;
    dp[1] = abs(stones[1] - stones[0]);
    for (int i = 2; i < n; i++) {
        int d1 = abs(stones[i] - stones[i-1]);
        int d2 = abs(stones[i] - stones[i-2]);
        dp[i] = min(d1 + dp[i-1], d2 + dp[i-2]);
    }
    cout << dp[n-1] << "\n";
    return 0;
}
