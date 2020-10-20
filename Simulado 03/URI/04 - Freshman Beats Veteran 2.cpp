/* Codigo adaptado a partir de:
 * https://github.com/malbolgee/URI/blob/master/1892.c
 * Não consegui encontrar o erro na minha versão, todos os casos de teste que tentei funcionavam.
 * Não apenas copiei, compreendi o código e tornei um pouco mais legivel. A abordagem é a mesma, mergesort.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 100100
typedef long long ll;

typedef struct {
	char s[15];
} string;

ll swaps;
string v[MAXSIZE];

void merge(string *, ll, ll *);

int main(int argc, char **argv)
{
    
	ll n, i;
	while (scanf("%lld", &n) != EOF)
	{
		swaps = 0;

		for (int i = 0; i < n; i++)
			scanf("%s", v[i].s);

		merge(v, n, &swaps);
		printf("%lld\n", swaps);
	}

	return 0;

}

void merge(string *start, ll length, ll *swaps)
{

	if (length > 1LL)
	{

		merge(start, length / 2LL, swaps);
		merge(start + (length / 2LL), (length + 1LL) / 2LL, swaps);
        
		ll i = 0LL, k;
		ll j = length / 2LL;
		string b[length];

		for (k = 0LL; k < length; ++k)
		{

			if (i < (length / 2LL) && j < length)
			{

				if (strcmp(start[i].s, start[j].s) < 0)
					b[k] = start[i], ++i;
				else if (strcmp(start[j].s, start[i].s) < 0)
					strcpy(b[k].s, start[j].s), ++j, *swaps += (length / 2LL) - i;
				else
					strcpy(b[k].s, start[i].s), ++i;
				
			}
			else if (i < (length / 2LL))
				strcpy(b[k].s, start[i].s), ++i;
			else
				strcpy(b[k].s, start[j].s), ++j;

		}

		memcpy(start, b, sizeof(string) * length);
	}

}