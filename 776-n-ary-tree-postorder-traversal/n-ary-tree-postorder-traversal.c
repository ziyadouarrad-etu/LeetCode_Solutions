/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorder(struct Node* root, int* returnSize) {
    int* result = malloc(10000 * sizeof(int));
    int i = 0;
    *returnSize = 0;

    int* helper(struct Node * root) {
        if (!root)
            return result;
        (*returnSize)++;
        for (int j = 0; j < root->numChildren; j++) {
            helper(root->children[j]);
        }
        result[i++] = root->val;
        return result;
    }
    return helper(root);
}