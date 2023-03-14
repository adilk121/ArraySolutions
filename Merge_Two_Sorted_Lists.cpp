//Merge Two Sorted Lists
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0); // create a dummy node
        ListNode* curr = dummy; // create a pointer to dummy node
        
        // loop until both lists are not empty
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                curr->next = l1; // add node from list1 to merged list
                l1 = l1->next; // move to next node in list1
            } else {
                curr->next = l2; // add node from list2 to merged list
                l2 = l2->next; // move to next node in list2
            }
            curr = curr->next; // move to next node in merged list
        }
        
        // add remaining nodes from list1
        while (l1 != NULL) {
            curr->next = l1;
            l1 = l1->next;
            curr = curr->next;
        }
        
        // add remaining nodes from list2
        while (l2 != NULL) {
            curr->next = l2;
            l2 = l2->next;
            curr = curr->next;
        }
        
        return dummy->next; // return the head of merged list
    }
};
