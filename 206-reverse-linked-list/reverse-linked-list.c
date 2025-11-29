/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* curr=head;
    struct ListNode* prev=NULL;
    struct ListNode* nextn=NULL;

    while(curr){
        nextn=curr->next;
        curr->next=prev;
        prev=curr;
        curr=nextn;
    }
    head=prev;
    return head;
}