/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (!p && !q)
        return true;
    if ((!p && q) || (p && !q))
        return false;
    if (p->val != q->val)
        return false;

    bool bool1, bool2;
    bool1 = isSameTree(p->left, q->left);
    bool2 = isSameTree(p->right, q->right);
    return bool1 && bool2;
}