#include <vector>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {

        int num_plots = flowerbed.size();
        if (num_plots < n * 2 - 1)
            return false;

        for (int i = 0; i < num_plots; ++i)
        {
            if (flowerbed[i] != 0)
                continue;
            bool left_ok = (i == 0) || (flowerbed[i-1] == 0);
            bool right_ok = (i == num_plots - 1) || (flowerbed[i+1] == 0);
            if (left_ok && right_ok)
            {
                n -= 1;
                flowerbed[i] = 1;
                if (n < 1) 
                    return true;
            }
        }
        return n < 1;
    }
};
