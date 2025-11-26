/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    char** result = malloc(n*sizeof(char*));
    *returnSize=n;

    for (int i = 1; i <= n; i++) {
        result[i-1]=malloc(9*sizeof(char));
        if (!(i % 5) && !(i % 3)) {
            sprintf(result[i-1], "FizzBuzz");
        }
        else if (!(i%3)){
            sprintf(result[i-1], "Fizz");
        }
        else if (!(i%5)){
            sprintf(result[i-1], "Buzz");
        }
        else{
            sprintf(result[i-1], "%d", i);
        }
    }
    return result;
}