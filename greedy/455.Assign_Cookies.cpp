#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int ans = 0;
        int cookie_idx = 0;
        while (ans < g.size() && cookie_idx < s.size()) {
            if (g[ans] <= s[cookie_idx])
                ++ans;
            ++cookie_idx;
        }
        return ans;
    }
};