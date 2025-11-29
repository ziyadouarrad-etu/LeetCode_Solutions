/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* p=head;
    struct ListNode* q=head;
    int len=0;

    // head alone edge case
    if (!head || !head->next)return NULL;

    // get the length of the linked list
    for (;p;p=p->next)len++;

    // len == n edge case
    if (len==n)return head->next;

    // remove nth node from the end
    p=head;
    for (int i=0; i<len-n; i++){
        q=p;
        p=p->next;
    }
    q->next=p->next;

    return head;
}