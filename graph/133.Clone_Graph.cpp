#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    Node* cloneGraph(Node* node) {
        //BFS
        if (node == nullptr)
            return nullptr;
        
        unordered_map<const Node*, Node*> copied;
        queue<const Node*> q({ node });
        copied[node] = new Node(node->val);
        while (!q.empty()) {
            const Node* curr = q.front();
            q.pop();
            for (auto neighbor : curr->neighbors) {
                if (copied.find(neighbor) == copied.end()) {
                    copied[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                copied[curr]->neighbors.push_back(copied[neighbor]);
            }
        }

        return copied[node];
    }
};
