#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100001

void processInput(char *input) {
    int startIndex = 0;
    int endIndex = strcspn(input, "[]");

    while (endIndex < strlen(input)) {
        if (input[endIndex] == '[') {
            startIndex = endIndex + 1;
        } else if (input[endIndex] == ']') {
            if (startIndex > 0) {
                printf("Beiju");
            }
            endIndex = strcspn(input + endIndex + 1, "[]");
            continue;
        }
        endIndex++;
    }
}

int main(void) {
    char input[MAX_SIZE];

    // Ler enquanto houver entrada do arquivo
    while (scanf("%s", input) != EOF) {
        processInput(input);
    }

    return 0;
}
