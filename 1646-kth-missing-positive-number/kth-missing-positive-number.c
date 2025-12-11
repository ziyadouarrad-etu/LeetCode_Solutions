int findKthPositive(int* arr, int arrSize, int k) {
    int i = 0, n = 1;

    while (k && i < arrSize) {
        if (n < arr[i])
            k -= 1;
        else
            i += 1;
        n += 1;
    }
    return n + k - 1;
}