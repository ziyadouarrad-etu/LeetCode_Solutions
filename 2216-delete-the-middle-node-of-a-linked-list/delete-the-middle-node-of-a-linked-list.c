/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* p = head;
    struct ListNode* q = head;
    int len = 0, mid;

    // head alone edge case
    if (!head || !head->next)
        return NULL;

    // get the length of the linked list
    for (; p; p = p->next)
        len++;

    // remove middle node
    mid = len / 2;
    p = head;
    for (int i = 0; i < mid; i++) {
        q = p;
        p = p->next;
    }
    q->next = p->next;

    return head;
}