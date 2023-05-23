#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        
        if (points.size() < 2)
            // return static_cast<int>(points.size());
            return points.size();
        
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b){
            return a[1] < b[1];
        });
        int min_arrows_required = 1; 
        int prev_end = points[0][1];
        for (int i = 1; i < points.size(); ++i)
        {
            if (points[i][0] > prev_end)
            {
                ++min_arrows_required;
                prev_end = points[i][1];
            }
        }
        return min_arrows_required;
    }
};
