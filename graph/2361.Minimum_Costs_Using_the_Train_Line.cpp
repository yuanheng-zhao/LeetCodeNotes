#include <vector>
#include <queue>
#include <utility>
#include <climits>

using namespace std;

class Solution {
public:
    vector<long long> minimumCosts(vector<int>& regular, vector<int>& express, int expressCost) {
        
        int num_of_stops = regular.size() + 1;

        vector<pair<int,int>> adj_graph[num_of_stops * 2];
        for (int i = 0; i < regular.size(); i++) {
            // auto p = make_pair(i+1, regular[i]);
            adj_graph[i].push_back(make_pair(i+1, regular[i]));
            adj_graph[i].push_back(make_pair(i + num_of_stops, expressCost));
        }
        for (int i = 0; i < express.size(); i++) {
            adj_graph[i + num_of_stops].push_back(make_pair(i + 1 + num_of_stops, express[i]));
            adj_graph[i + num_of_stops].push_back(make_pair(i, 0));
        }

        int dist_to[num_of_stops * 2];
        dist_to[0] = 0;
        for (int i = 1; i < num_of_stops * 2; i++) {
            dist_to[i] = INT_MAX;
        }
        priority_queue<pair<int, int>> pq;
        pq.push(make_pair(0, 0));
        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();
            int distance = p.first;
            int from = p.second;
            for (auto & p2: adj_graph[from]) {
                int to = p2.first;
                int cost = p2.second;
                if (dist_to[from] + cost < dist_to[to]) {
                    dist_to[to] = dist_to[from] + cost;
                    pq.push(make_pair(dist_to[to], to));
                }
            }
        }

        vector<long long> res;
        for (int i = 0; i < num_of_stops; i++) {
            res.push_back(min(dist_to[i], dist_to[i + num_of_stops]));
        }
        res.erase(res.begin());
        return res;
    }
};
