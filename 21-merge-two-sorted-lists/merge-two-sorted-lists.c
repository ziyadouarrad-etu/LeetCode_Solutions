/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* result=(struct ListNode*)malloc(sizeof(struct ListNode));
    result->next=NULL;
    struct ListNode* r=result;
    struct ListNode* p=list1;
    struct ListNode* q=list2;
    while(p && q){
        r->next=(struct ListNode*)malloc(sizeof(struct ListNode));
        r=r->next;
        r->next=NULL;
        if (p->val<q->val){
            r->val=p->val;
            p=p->next;
        }
        else{
            r->val=q->val;
            q=q->next;
        }
    }
    while(p){
        r->next=(struct ListNode*)malloc(sizeof(struct ListNode));
        r=r->next;
        r->next=NULL;
        r->val=p->val;
        p=p->next;
    }
    while(q){
        r->next=(struct ListNode*)malloc(sizeof(struct ListNode));
        r=r->next;
        r->next=NULL;
        r->val=q->val;
        q=q->next; 
    }
    return result->next;
}