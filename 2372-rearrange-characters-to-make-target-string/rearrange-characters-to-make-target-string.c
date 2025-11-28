int rearrangeCharacters(char* s, char* target) {
    int num_copies = 0;
    bool found;
    while (true) {
        for (int i = 0; target[i] != '\0'; i++) {
            found = false;
            for (int j = 0; s[j] != '\0'; j++) {
                if (target[i] == s[j]) {
                    found = true;
                    s[j] = '.';
                    break;
                }
            }
            if (!found)
                return num_copies;
        }
        num_copies++;
    }
    return num_copies;
}