/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {

    int* result = malloc(2 * sizeof(int));
    result[0]=-1;
    result[1]=-1;
    int a = 0, b = numsSize - 1, c, first=-1, last=-1;
    *returnSize = 2;

    //We first locate the first occurence
    while (a<=b){
        c=(a+b)/2;
        if (nums[c]<target)a=c+1;
        else if (nums[c]>target)b=c-1;
        else{
            first=c;
            b=c-1;
        }
    }

    //Then we find the last occurence
    a = 0, b = numsSize - 1;

    while (a<=b){
        c=(a+b)/2;
        if (nums[c]<target)a=c+1;
        else if (nums[c]>target)b=c-1;
        else{
            last=c;
            a=c+1;
        }
    }
    result[0]=first;
    result[1]=last;
    return result;
}

