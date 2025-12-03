/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    int ld, rd;
    if (!root)return 0;
    ld=1+maxDepth(root->left);
    rd=1+maxDepth(root->right);
    return ld>rd?ld:rd;
}