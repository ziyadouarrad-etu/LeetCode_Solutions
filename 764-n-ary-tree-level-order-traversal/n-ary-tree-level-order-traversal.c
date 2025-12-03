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
    // Malloc necessary arrays
    int** result = malloc(1000 * sizeof(int*));
    int* columnSizes = malloc(1000 * sizeof(int));
    *returnColumnSizes = columnSizes;

    // Initialize *returnSize and handle empty tree edge case
    *returnSize = 0;
    if (!root)
        return result;

    /* In this solution we will use a queue to keep track of children
    The logic is to that in each iteration we will have the current level nodes
    in the queue, the when a node is treated (its val is gathered and all its
    children added to end of queue), we will we will move forward to the next
    node in the queue.
    */
    struct Node** queue = malloc(10001 * sizeof(struct Node*));
    int head = 0, tail = 0, i, j, temp;
    queue[tail++] = root;
    while (head < tail) {
        columnSizes[*returnSize] = tail - head;
        result[*returnSize] = malloc(columnSizes[*returnSize] * sizeof(int));
        temp = tail;
        for (i = head; i < temp; i++) {
            result[*returnSize][i - head] = queue[i]->val;
            for (j = 0; j < queue[i]->numChildren; j++) {
                queue[tail++] = queue[i]->children[j];
            }
        }
        head = i;
        (*returnSize)++;
    }
    return result;
}