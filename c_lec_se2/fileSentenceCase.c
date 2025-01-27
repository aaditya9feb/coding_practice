#include <stdio.h>
#include <ctype.h>

void toSentenceCase(char *str) {
    int i = 0;
    int capitalize = 1;

    while (str[i]) {
        if (capitalize && isalpha(str[i])) {
            str[i] = toupper(str[i]);
            capitalize = 0;
        } else {
            str[i] = tolower(str[i]);
        }

        if (str[i] == '.' || str[i] == '!' || str[i] == '?') {
            capitalize = 1;
        }

        i++;
    }
}

int main() {
    char input[1000];
    FILE *file;

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);

    file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fputs(input, file);
    fclose(file);

    toSentenceCase(input);

    file = fopen("output.txt", "a");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fputs("\nSentence case:\n", file);
    fputs(input, file);
    fclose(file);

    printf("String written to file in sentence case.\n");

    return 0;
}