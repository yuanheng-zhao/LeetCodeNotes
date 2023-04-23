#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> graph(numCourses, vector<int>());
        vector<bool> visited(numCourses, false);
        stack<int> st;

        // build adjacency list (graph)
        for (auto const& prereq : prerequisites) {
        // for (const vector<int>& prereq : prerequisites) {
            int f = prereq[1];
            int t = prereq[0];
            graph[f].push_back(t);
        }
        // topological sort (or kind of?)
        for (int i = 0; i < numCourses; ++i) {
            topological(graph, visited, st, i);
        }

        // decode order
        int count = 0;
        vector<int> order(numCourses);
        while (!st.empty()) {
            order[st.top()] = count++;
            st.pop();
        }

        // check any conflicts
        for (auto const& prereq : prerequisites) {
            // int f = prereq[1];
            // int t = prereq[0];
            if (order[prereq[0]] <= order[prereq[1]])
                return false;
        }

        return true;
    }

private:
    void topological(vector<vector<int>>& adj_graph, vector<bool>& visited, stack<int>& st, int i) {
        if (visited[i])
            return;
        visited[i] = true;
        for (int t : adj_graph[i]) {
            topological(adj_graph, visited, st, t);
        }
        st.push(i);
    }
};