#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        // The tests are generated such that there is exactly one solution. 
        int l = 0, r = numbers.size() - 1, sum = 0;
        while (l < r)
        {
            sum = numbers[l] + numbers[r];
            if (sum == target)
                break;
            if (sum < target)
                ++l;
            else
                --r;
        }
        return vector<int>{l + 1, r + 1};
    }
};
