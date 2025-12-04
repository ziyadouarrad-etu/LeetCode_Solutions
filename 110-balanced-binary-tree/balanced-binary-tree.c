/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>

int height(struct TreeNode* root) {
    if (!root)
        return -1;
    int left = height(root->left);
    int right = height(root->right);
    return 1 + (left > right ? left : right);
}

bool isBalanced(struct TreeNode* root) {
    if (!root)
        return true;
    if (abs(height(root->left) - height(root->right)) > 1)
        return false;

    return isBalanced(root->left) && isBalanced(root->right);
}