#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        
        int ans = 0;
        vector<int> candy_allocated(ratings.size(), 1);  // Each child must have at least one candy

        for (int i = 1; i < ratings.size(); ++i) // left to right
        {
            if (ratings[i] > ratings[i-1])
                candy_allocated[i] = candy_allocated[i-1] + 1;
        }
        for (int i = ratings.size() - 2; i >= 0; --i)  // then right to left
        {
            if (ratings[i] > ratings[i+1] && candy_allocated[i] <= candy_allocated[i+1])
                candy_allocated[i] = candy_allocated[i+1] + 1;
        }

        for (int candy_given : candy_allocated)
            ans += candy_given;
        return ans;
    }
};
