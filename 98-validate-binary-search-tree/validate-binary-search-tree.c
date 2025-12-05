/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isValidBST(struct TreeNode* root) {
    int* a = NULL;
    int n;
    bool helper(struct TreeNode * root) {
        if (!root)
            return true;
        if (!helper(root->left))
            return false;
        if (a && *a >= root->val)
            return false;
        n = root->val;
        a = &n;
        if (!helper(root->right))
            return false;
        return true;
    }
    return helper(root);
}