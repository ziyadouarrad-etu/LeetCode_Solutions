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
bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) {
    if (isSameTree(root, subRoot))
        return true;
    bool bool1 = false, bool2 = false;
    if (root->left)
        bool1 = isSubtree(root->left, subRoot);
    if (root->right)
        bool2 = isSubtree(root->right, subRoot);
    return bool1 || bool2;
}