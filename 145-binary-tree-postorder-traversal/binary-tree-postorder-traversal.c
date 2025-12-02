/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    int* result = malloc(100 * sizeof(int));
    int i = 0;
    *returnSize = 0;

    int* helper(struct TreeNode * root) {
        if (!root)
            return result;
        helper(root->left);
        helper(root->right);
        result[i++] = root->val;
        (*returnSize)++;
        return result;
    }

    return helper(root);
}