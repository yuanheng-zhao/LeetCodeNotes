#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:

    bool satisfy(const unordered_map<char, int>& m) {
        for (auto const& pair : m)
        {
            if (pair.second > 0) 
                return false;
        }
        return true;
    }

    string minWindow(string s, string t) {
        
        if (s.length() < t.length())
            return "";

        // counter indicates the number of chars required at the moment, negative means we have extra
        unordered_map<char, int> counter;
        int l = 0, ans_l = 0, ans_r = s.length();
        // record all chars in string t into the counter map
        for (auto &c : t)
        {
            if (counter.find(c) == counter.end()) 
                counter[c] = 0;
            ++counter[c];
        }
        // window the starting substring of s with the same legnth as t minus 1
        for (int i = 0; i < t.length() - 1; ++i)
        {
            if (counter.find(s.at(i)) != counter.end())
                --counter[s.at(i)];
        }
        for (int r = t.length() - 1; r < s.length(); ++r)
        {
            if (counter.find(s.at(r)) != counter.end())
                --counter[s.at(r)];
            // remove unnecessary chars to shorten the length of possible ans
            while (l < r)
            {
                if (counter.find(s.at(l)) != counter.end())
                {
                    if (counter[s.at(l)] < 0)
                        ++counter[s.at(l)];
                    else
                        break;
                }
                ++l;
            }
            if (satisfy(counter) && r - l < ans_r - ans_l)
            {
                ans_l = l;
                ans_r = r;
            }
        }

        if (ans_r - ans_l >= s.length())
            return "";
        return s.substr(ans_l, ans_r - ans_l + 1);
    }
};


// Notes: could use vector to indicate number of chars required instead of using hash table
// e.g. 
// vector<int> counter(128, 0);  // ascii encoded values
// vector<bool> exists(128, false);
