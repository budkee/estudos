#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STRINGS 50
#define MAX_STRING_LENGTH 50

char strings[MAX_STRINGS][MAX_STRING_LENGTH];

int compare(const void *a, const void *b) {
    const char *str1 = *(const char **)a;
    const char *str2 = *(const char **)b;

    if (strlen(str1) < strlen(str2)) {
        return -1;
    } else if (strlen(str1) > strlen(str2)) {
        return 1;
    } else {
        return strcmp(str1, str2);
    }
}

int main(void) {
    int t; // Número de conjuntos de strings
    scanf("%d", &t);
    getchar(); // Consume a newline character after reading t

    while (t--) {
        int num_strings = 0;

        // Read and store the strings
        char input[MAX_STRING_LENGTH];
        while (1) {
            if (fgets(input, sizeof(input), stdin) == NULL || input[0] == '\n') {
                break;
            }

            input[strcspn(input, "\n")] = '\0'; // Remove newline character if present
            strncpy(strings[num_strings], input, sizeof(strings[num_strings]) - 1);
            strings[num_strings][sizeof(strings[num_strings]) - 1] = '\0'; // Garanta que a string esteja terminada
            num_strings++;
        }

        // Create an array of pointers to strings
        const char *string_ptrs[MAX_STRINGS];
        for (int i = 0; i < num_strings; i++) {
            string_ptrs[i] = strings[i];
        }

        // Sort the array of string pointers
        qsort(string_ptrs, num_strings, sizeof(const char *), compare);

        // Print the sorted strings
        for (int i = 0; i < num_strings; i++) {
            printf("%s", string_ptrs[i]);
            if (i < num_strings - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}
