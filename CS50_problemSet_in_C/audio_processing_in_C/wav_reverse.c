#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char* argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse INPUTFILENAME OUTPUTFILENAME\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE* infile = fopen(argv[1], "rb");
    if (infile == NULL)
    {
        printf("Can't read file!\n");
        return 2;
    }

    // Read header
    // TODO #3
    WAVHEADER* waveheader = malloc(44);
    fread(waveheader, sizeof(BYTE), 44, infile);

    // Use check_format to ensure WAV format
    // TODO #4
    int is_wave = check_format(*waveheader);

    if (is_wave != 0)
    {
        fclose(infile);
        return 3;
    }

    // Open output file for writing
    // TODO #5
    FILE* outfile = fopen(argv[2], "w");
    if (outfile == NULL)
    {
        printf("Can't write to %s\n", argv[2]);
        return 4;
    }

    // Write header to file
    // TODO #6
    fwrite(waveheader, sizeof(BYTE), 44, outfile);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(*waveheader);

    // Write reversed audio to file
    // TODO #8
    BYTE* buffer = malloc(block_size * sizeof(BYTE));;

    fseek(infile, 0 - block_size, SEEK_END);

    while (ftell(infile) > sizeof(*waveheader) - block_size)
    {
        fread(buffer, block_size, 1, infile);
        fwrite(buffer, block_size, 1, outfile);
        fseek(infile, 0 - (block_size * 2), SEEK_CUR); // if seek is half of block_size, you can create audio slowdown effect
    }

    fclose(infile);
    fclose(outfile);

    free(waveheader);
    free(buffer);

    return 0;
}

int check_format(WAVHEADER header)
{
    // TODO #4
    int wave[] = { 0x57, 0x41, 0x56, 0x45 };

    for (int i = 0; i < 4; i++)
    {
        if (header.format[i] != wave[i])
        {
            printf("Not a valid WAVE file!\n");
            return 1;
        }
    }

    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int block_size = header.numChannels * (header.bitsPerSample / 8);
    return block_size;
}