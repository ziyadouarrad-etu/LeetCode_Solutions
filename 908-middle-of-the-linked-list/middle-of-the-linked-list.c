/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;

    // head alone edge case
    if (!head->next)
        return head;
    
    // return the middle
    while(fast->next && fast->next->next){
        fast=fast->next->next;
        slow=slow->next;
    }
    return slow->next;
    
}