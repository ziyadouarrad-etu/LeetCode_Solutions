/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root) {
    int ld = 0, rd = 0, min;
    if (!root)
        return 0;
    if (!root->left && !root->right)
        return 1;
    if (root->left)
        ld = 1 + minDepth(root->left);
    if (root->right)
        rd = 1 + minDepth(root->right);

    if (ld && rd)
        min = ld < rd ? ld : rd;
    else if (ld)
        min = ld;
    else
        min = rd;
    return min;
}