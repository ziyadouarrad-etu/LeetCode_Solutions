int removeElement(int* nums, int numsSize, int val) {
    int end = numsSize-1, i=0, taille=0, temp;
    while (i<numsSize){
        if (i>end)break;
        if (nums[i]==val){
            temp=nums[i];
            nums[i]=nums[end];
            nums[end]=temp;
            end--;
            if (end<0)break;
        }
        else{
            i++;
            taille++;
        }
    }
    return taille;
}