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
    if ((p->left && !q->left) || (p->right && !q->right))
        return false;
    if ((q->left && !p->left) || (q->right && !p->right))
        return false;
    bool bool1 = true, bool2 = true;
    if (p->left)
        bool1 = isSameTree(p->left, q->left);
    if (p->right)
        bool2 = isSameTree(p->right, q->right);
    return bool1 && bool2;
}