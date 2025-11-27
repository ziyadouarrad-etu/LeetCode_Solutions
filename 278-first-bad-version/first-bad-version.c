// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int a = 1, b = n, c;
    while (a < b) {
        c = a + (b - a) / 2;
        if (isBadVersion(c))
            b = c;
        else
            a = c + 1;
    }
    return b;
}