#include <stdio.h>
#include <stdlib.h>

void create_and_write_file(const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    fprintf(file, "Hello, this is a test file.\n");
    fprintf(file, "This file is created and written by the program.\n");

    fclose(file);
}

void display_file(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
}

void append_to_file(const char *filename) {
    FILE *file = fopen(filename, "a");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    fprintf(file, "Appending a new line to the file.\n");

    fclose(file);
}

void selector_interface() {
    int choice;
    const char *filename = "testfile.txt";

    while (1) {
        printf("\nMenu:\n");
        printf("1. Create and write to file\n");
        printf("2. Display file contents\n");
        printf("3. Append to file\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                create_and_write_file(filename);
                printf("File created and written successfully.\n");
                break;
            case 2:
                display_file(filename);
                break;
            case 3:
                append_to_file(filename);
                printf("File appended successfully.\n");
                break;
            case 4:
                exit(EXIT_SUCCESS);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}

int main() {
    selector_interface();
    return 0;
}