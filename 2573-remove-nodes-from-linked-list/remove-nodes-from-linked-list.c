/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNodes(struct ListNode* head) {
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    struct ListNode* nextn = NULL;
    struct ListNode* newHead = NULL;
    int max;
    
    // Inversing the list
    while (curr) {
        nextn = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextn;
    }
    head = prev;

    // Iterating thgouth the reversed list saving the max nodes
    newHead = malloc(sizeof(struct ListNode));
    newHead->val = head->val;
    newHead->next=NULL;

    curr = head->next;
    max = newHead->val;
    while (curr) {
        if (curr->val >= max) {
            nextn = malloc(sizeof(struct ListNode));
            nextn->val = curr->val;
            nextn->next = newHead;
            newHead = nextn;
            max=curr->val;
        }
        curr = curr->next;
    }

    return newHead;
}