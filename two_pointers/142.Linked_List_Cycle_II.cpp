/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <stdlib.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        
        ListNode *slow = head;
        ListNode *fast = head;
        do
        {
            if (!fast || !fast->next) return nullptr;  // no cycle detected
            slow = slow->next;
            fast = fast->next->next;
        } while (fast != slow);
        
        // refer to notes in GoodNotes 2020
        fast = head;
        while (fast != slow)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
