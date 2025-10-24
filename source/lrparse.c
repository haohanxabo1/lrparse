#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//dynamic list of strings 
typedef struct {
    char **items;
    size_t count;
} StringList;

static void sl_init(StringList *sl) { sl->items = NULL; sl->count = 0; }

static void sl_free(StringList *sl) {
    if (!sl) return;
    for (size_t i = 0; i < sl->count; ++i) free(sl->items[i]);
    free(sl->items);
    sl->items = NULL; sl->count = 0;
}

static void sl_add_slice(StringList *sl, const char *p, size_t len) {
    char *cpy = (char*)malloc(len + 1);
    if (!cpy) return;
    memcpy(cpy, p, len);
    cpy[len] = '\0';
    sl->items = (char**)realloc(sl->items, (sl->count + 1) * sizeof(char*));
    if (!sl->items) { free(cpy); sl->count = 0; return; }
    sl->items[sl->count++] = cpy;
}

static void sl_add_cstr(StringList *sl, const char *s) {
    sl_add_slice(sl, s, strlen(s));
}
// normal mode : first match
StringList lr(const char *s, const char *left, const char *right)
{
    StringList out; sl_init(&out);
    if (!s || !left || !right) return out;

    size_t n  = strlen(s);
    size_t nl = strlen(left);
    size_t nr = strlen(right);

    if (nl == 0 && nr == 0) { sl_add_cstr(&out, s); return out; }

    // find left boundary
    const char *pL = (nl == 0) ? s : strstr(s, left);
    if (!pL) return out;
    const char *start = pL + nl;

    // find right boundary
    const char *pR = (nr == 0) ? (s + n) : strstr(start, right);
    if (!pR) return out;

    sl_add_slice(&out, start, (size_t)(pR - start));
    return out;
}
// recursive
StringList lrr(const char *s, const char *left, const char *right)
{
    StringList out; sl_init(&out);
    if (!s || !left || !right) return out;

    size_t n  = strlen(s);
    size_t nl = strlen(left);
    size_t nr = strlen(right);

    if (nl == 0 && nr == 0) { sl_add_cstr(&out, s); return out; }

    const char *pos = s;
    while (pos < s + n) {
        const char *pL = (nl == 0) ? pos : strstr(pos, left);
        if (!pL) break;
        const char *start = pL + nl;

        const char *pR = (nr == 0) ? (s + n) : strstr(start, right);
        if (!pR) break;

        sl_add_slice(&out, start, (size_t)(pR - start));

        if (nr == 0) break;            
        pos = pR + nr;                   
    }
    return out;
}


int main(void) {


    StringList c = lr("a cake make punch", " ", " ");          
    for (size_t i = 0; i < c.count; ++i) printf("lrr: %s\n", c.items[i]);
    sl_free(&c);
    return 0;
}

