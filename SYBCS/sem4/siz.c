#include <stdio.h>
#include <stdlib.h>

void main() {
    char a = 'a';
    char *ptr = &a;

    printf("Size of int variable a: %zu bytes\n", sizeof(a));
    printf("Size of int pointer ptr: %zu bytes\n", sizeof(*ptr));
}