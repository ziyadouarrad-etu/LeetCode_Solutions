/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */
int** levelOrder(struct Node* root, int* returnSize, int** returnColumnSizes) {
    int** result = malloc(1000 * sizeof(int*));
    int* columnSizes = malloc(1000 * sizeof(int));
    *returnColumnSizes = columnSizes;

    struct Node** curr = malloc(10001 * sizeof(struct Node*));
    struct Node** next = malloc(10001 * sizeof(struct Node*));
    int* temp = malloc(10000 * sizeof(int));
    int i, j, k = 0, c;

    *returnSize = 0;
    if (!root)
        return result;

    curr[0] = root;
    curr[1] = NULL;
    while (curr[0]) {
        c = 0;
        for (i = 0; curr[i]; i++) {
            temp[i] = curr[i]->val;
            for (j = 0; j < curr[i]->numChildren; j++) {
                next[c++] = (curr[i]->children)[j];
            }
            next[c] = NULL;
        }

        result[k] = malloc(i * sizeof(int));
        for (j = 0; j < i; j++)
            result[k][j] = temp[j];
        (*returnColumnSizes)[k++] = i;
        (*returnSize)++;
        for (i = 0; next[i]; i++) {
            curr[i] = next[i];
        }
        curr[i] = NULL;
    }
    free(curr);
    free(next);
    free(temp);
    return result;
}