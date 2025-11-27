bool canConstruct(char* ransomNote, char* magazine) {
    int i, j;
    bool flag;
    for (i=0; ransomNote[i]!='\0';i++){
        flag=0;
        for (j=0; magazine[j]!='\0';j++){
            if (ransomNote[i]==magazine[j]){
                magazine[j]='.';
                flag=1;
                break;
            }
        }
        if (!flag)return 0;
    }
    return 1;
}