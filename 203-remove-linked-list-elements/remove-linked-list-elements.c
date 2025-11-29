/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* createNode(int val) {
    struct ListNode* res = malloc(sizeof(struct ListNode));
    res->val = val;
    res->next = NULL;
    return res;
}
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* newHead = NULL;
    struct ListNode* curr = newHead;
    struct ListNode* temp = NULL;
    for (struct ListNode* p = head; p; p = p->next) {
        if (p->val == val)
            continue;
        temp = createNode(p->val);
        if (!newHead)
            newHead = temp;
        else
            curr->next = temp;
        curr = temp;
    }
    return newHead;
}