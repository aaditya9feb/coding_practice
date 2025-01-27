#include <stdio.h>

int main() {
    int asciiCode;

    // Prompt user for ASCII code
    printf("Enter an ASCII code (0-127): ");
    scanf("%d", &asciiCode);

    // Check if the input is within the valid ASCII range
    if (asciiCode >= 0 && asciiCode <= 127) {
        // Convert ASCII code to its corresponding symbol
        char symbol = (char)asciiCode;
        printf("The symbol for ASCII code %d is '%c'\n", asciiCode, symbol);
    } else {
        printf("Invalid ASCII code. Please enter a value between 0 and 127.\n");
    }

    return 0;
}