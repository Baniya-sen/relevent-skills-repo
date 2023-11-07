#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define MAX_LENGTH 45

// Prototypes
bool check_word(const char* word);
unsigned int hash(const char* word);
bool load_in(const char *dictionary);
unsigned int get_size(void);
bool unload_mem(void);

#endif  // DICTIONARY_H