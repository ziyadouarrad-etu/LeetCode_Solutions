/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
int guess(int num);

int guessNumber(int n) {
    int a = 1, b = n, c;
    do {
        c = a + (b - a) / 2;
        if (!guess(c))
            break;
        else if (guess(c) == 1)
            a = c + 1;
        else
            b = c - 1;
    } while (a <= b);
    return c;
}