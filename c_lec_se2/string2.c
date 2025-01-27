#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void strncpy_custom(char *dest, const char *src, size_t n) {
    size_t i;
    for (i = 0; i < n && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    for (; i < n; i++) {
        dest[i] = '\0';
    }
}

int main() {
    char src[100];
    char dest[100];
    size_t n;

    printf("Enter the source string: ");
    gets(src); // Note: gets is unsafe and should not be used in production code

    printf("Enter the number of characters to copy: ");
    scanf("%zu", &n);

    strncpy_custom(dest, src, n);
    printf("Copied string: %s\n", dest);

    return 0;
}
