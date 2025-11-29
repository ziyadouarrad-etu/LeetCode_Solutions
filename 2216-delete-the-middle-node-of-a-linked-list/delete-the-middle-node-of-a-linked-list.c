/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;

    // head alone edge case
    if (!head || !head->next)
        return NULL;

    // remove middle node
    while (fast->next && fast->next->next) {
        fast = fast->next->next;
        slow = slow->next;
    }
    slow->next = slow->next->next;
    return head;
}