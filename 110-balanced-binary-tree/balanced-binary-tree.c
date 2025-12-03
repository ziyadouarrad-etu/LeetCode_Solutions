/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>

int maxDepth(struct TreeNode* root) {
    int ld, rd;
    if (!root)
        return 0;
    ld = 1 + maxDepth(root->left);
    rd = 1 + maxDepth(root->right);
    return ld > rd ? ld : rd;
}

bool isBalanced(struct TreeNode* root) {
    if (!root)
        return true;
    if (!root->left)
        return maxDepth(root) <= 2;
    if (!root->right)
        return maxDepth(root) <= 2;
    return abs(maxDepth(root->left) - maxDepth(root->right)) <= 1 &&
               isBalanced(root->left) && isBalanced(root->right);
}