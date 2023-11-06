#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define block_size 512

typedef uint8_t byte;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./image_recover IMAGE\n");
        return 1;
    }

    FILE* infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Can't read file\n");
        return 2;
    }

    byte* buffer = malloc(block_size);
    if (buffer == NULL)
    {
        printf("Memory allocation failed\n");
        return 3;
    }

    char names[8];
    int value = 0;
    FILE* outfile = NULL;

    while (fread(buffer, 1, block_size, infile) == block_size)
    {
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF)
        {
            if (outfile != NULL)
            {
                fclose(outfile);
            }

            sprintf(names, "%03d.jpg", value);
            outfile = fopen(names, "w");
            if (outfile == NULL)
            {
                printf("Could not write to .jpg file\n");
                return 4;
            }
            value++;
        }

        if (outfile != NULL)
        {
            fwrite(buffer, 1, block_size, outfile);
        }
    }

    if (outfile != NULL)
    {
        fclose(outfile);
    }

    fclose(infile);
    free(buffer);
    return 0;
}