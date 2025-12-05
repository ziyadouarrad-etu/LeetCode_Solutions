/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int findSecondMinimumValue(struct TreeNode* root) {
    int min = root->val, min2 = -1;
    void helper(struct TreeNode * root) {
        if (!root->left)
            return;
        bool left = true, right = true;
        int temp;
        if (root->left->val > root->val) {
            left = false;
            if (min2 == -1)
                min2 = root->left->val;
            else
                min2 = min2 < root->left->val ? min2 : root->left->val;
        }
        if (root->right->val > root->val) {
            right = false;
            if (min2 == -1)
                min2 = root->right->val;
            else
                min2 = min2 < root->right->val ? min2 : root->right->val;
        }
        if (left)
            helper(root->left);
        if (right)
            helper(root->right);
    }
    helper(root);
    return min2;
}