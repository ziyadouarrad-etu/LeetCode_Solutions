char* firstPalindrome(char** words, int wordsSize) {
    bool is_pal;
    int size, mid;
    char* result = malloc(101 * sizeof(char));
    result[0] = '\0';

    for (int i = 0; i < wordsSize; i++) {
        size = 0;
        for (int j = 0; words[i][j] != '\0'; j++) {
            size++;
        }
        mid = (size-1) / 2;

        is_pal = true;
        for (int j = 0; j <= mid; j++) {
            if (words[i][j] != words[i][size - j - 1]){
                is_pal = false;
                break;
            }
        }
        if (is_pal) {
            sprintf(result, words[i]);
            break;
        }
    }
    return result;
}