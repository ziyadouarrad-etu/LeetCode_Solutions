/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int hash1(int val, int numsSize){
    return val%numsSize;
}

bool in_list(struct ListNode* hashTable[], int numsSize, int val) {
    struct ListNode* p=hashTable[hash1(val, numsSize)];
    while (p){
        if (p->val==val) return true;
        p=p->next;
    }
    return false;
}
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    struct ListNode* hashTable[numsSize];
    for (int i=0;i<numsSize;i++)hashTable[i]=NULL;
    struct ListNode* p=NULL;

    for(int i=0;i<numsSize;i++){
        if (!hashTable[hash1(nums[i], numsSize)]){
            hashTable[hash1(nums[i], numsSize)]=malloc(sizeof(struct ListNode));
            hashTable[hash1(nums[i], numsSize)]->val=nums[i];
            hashTable[hash1(nums[i], numsSize)]->next=NULL;
        }
        else{
            for (p=hashTable[hash1(nums[i], numsSize)]; p->next; p=p->next);
            p->next=malloc(sizeof(struct ListNode));
            p->next->val=nums[i];
            p->next->next=NULL;
        }
    }


    while (head && in_list(hashTable, numsSize, head->val)) {
        head = head->next;
    }

    p = head;
    while (p && p->next) {
        if (in_list(hashTable, numsSize, p->next->val)) {
            p->next = p->next->next;
        } else
            p = p->next;
    }

    return head;
}