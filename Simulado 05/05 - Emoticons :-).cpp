#include <stdio.h>
#include <string.h>

int main()
{
    while (1) {
        char line[82], emoticons[100][17];
        int N, M, index[100], count = 0;
        int i, j, k;

        // Read number of emoticons and lines
        scanf("%d%d", &N, &M);
        getchar();

        // If 0 0, end of input
        if (!N && !M)
            break;

        // Read emoticons
        for (i = 0; i < N; i++) {
            fgets(emoticons[i], 17, stdin);
            emoticons[i][strlen(emoticons[i]) - 1] = '\0';
        }

        // Read each line and count char substitutions
        for (i = 0; i < M; i++) {
            // Read line
            fgets(line, 82, stdin);

            // Reset emoticon indexes
            memset(index, 0, sizeof(index));

            // For each char in line, compare to all emoticon
            for (j = 0; line[j] != '\n'; j++) {
                // For each emoticon
                for (k = 0; k < N; k++) {
                    // If char matches, increase index
                    if (line[j] == emoticons[k][index[k]])
                        ++index[k];
                    // If char does not match, set index to 1 if it matches first char, else set it to 0
                    else
                        index[k] = (line[j] == emoticons[k][0]);

                    // If line contains emote
                    if (index[k] == strlen(emoticons[k])) {
                        // Replace last char of emote with ' ' and increase count
                        line[j] = ' ';
                        count++;
                        // Reset emoticon indexes
                        memset(index, 0, sizeof(index));
                    }
                }
            }
        }
        // Print result
        printf("%d\n", count);
    }

    return 0;
}