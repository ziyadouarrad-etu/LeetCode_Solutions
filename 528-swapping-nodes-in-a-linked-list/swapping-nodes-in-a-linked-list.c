/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode* p = head;
    struct ListNode* q = head;

    int len=0, temp;
    for (;p;p=p->next)len++;

    p = head;
    for (int i = 0; i < k-1; i++)p=p->next;
    for (int i = 0; i < len-k; i++)q=q->next;

    temp=p->val;
    p->val=q->val;
    q->val=temp;
    return head;
}