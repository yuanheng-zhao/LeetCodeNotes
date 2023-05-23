#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        if (intervals.size() < 2)
            return 0;
        
        // 1) Use LIS, O(N^2), might exceed time limits for some tests
        // Solution skipped here

        // 2) Greedy: consider to retain interval with sooner/earlier end time
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){
            return a[1] < b[1];
        });
        int non_overlapping_count = 1;
        int prev_end_time = intervals[0][1];
        for (int i = 1; i < intervals.size(); ++i)
        {
            if (intervals[i][0] >= prev_end_time)
            {
                prev_end_time = intervals[i][1];
                ++non_overlapping_count;
            }
        }
        return intervals.size() - non_overlapping_count;
    }
};
