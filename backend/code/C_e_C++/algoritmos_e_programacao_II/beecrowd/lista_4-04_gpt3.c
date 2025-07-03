#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 1000

typedef struct {
    char character;
    int frequency;
} CharFrequency;

int compare(const void *a, const void *b) {
    CharFrequency *charA = (CharFrequency *)a;
    CharFrequency *charB = (CharFrequency *)b;

    if (charA->frequency == charB->frequency) {
        return charB->character - charA->character;
    }

    return charA->frequency - charB->frequency;
}

int main(void) {
    char line[MAX_LENGTH];

    while (fgets(line, MAX_LENGTH, stdin)) {
        int frequencies[256] = {0}; // Initialize an array to store character frequencies

        // Count character frequencies
        for (int i = 0; line[i] != '\0' && line[i] != '\n'; i++) {
            frequencies[(int)line[i]]++;
        }

        CharFrequency charFreq[256]; // Create a structure array to store character and frequency pairs
        int count = 0;

        // Populate the character frequency structure
        for (int i = 32; i < 128; i++) {
            if (frequencies[i] > 0) {
                charFreq[count].character = (char)i;
                charFreq[count].frequency = frequencies[i];
                count++;
            }
        }

        // Sort the structure array
        qsort(charFreq, count, sizeof(CharFrequency), compare);

        // Print the results
        for (int i = 0; i < count; i++) {
            printf("%d %d\n", (int)charFreq[i].character, charFreq[i].frequency);
        }

        printf("\n"); // Print a blank line to separate output for different test cases
    }

    return 0;
}
