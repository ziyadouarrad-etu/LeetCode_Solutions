/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* result=(struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* p=l1;
    struct ListNode* q=l2;
    struct ListNode* r=result;
    int sum, residue=0, dec;

    while (p || q || residue){
        sum=residue;
        if (p){
            sum+=p->val;
            p=p->next;
        }
        if (q){
            sum+=q->val;
            q=q->next;
        }
        residue=sum/10;
        r->val=sum%10;
        if (p || q || residue){
            r->next=(struct ListNode*)malloc(sizeof(struct ListNode));
            r=r->next;
        }
        r->next=NULL;
    }
    return result;
}