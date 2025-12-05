/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int kthSmallest(struct TreeNode* root, int k) {
    int count = k;
    int a;
    void helper(struct TreeNode * root) {
        if (!root || !count)
            return;
        helper(root->left);
        if (count) {
            a = root->val;
            count--;
            helper(root->right);
        }
    }
    helper(root);
    return a;
}