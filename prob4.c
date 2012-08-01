#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void itoa(int, char []);
void reverse(char []);
int findPal();

int main()
{
  printf("Biggest palindrome: %d\n", findPal());
  return 0;
}

int findPal(){
  char buff[10],revbuff[20];
  int newmax = 0;
  int i,j,k;
  for(j = 999; j > 100; j--)
    {
      for(k = j-1; k > 100; k--)
      {
	  i = j*k;
	  itoa(i, buff);
	  int c = 0;
	  do{
	    revbuff[c] = buff[c];
	    c++;
	  }while(buff[c] != '\0');
	  revbuff[c] = '\0';
	  reverse(revbuff);
	  
	  if(strcmp(revbuff, buff) == 0)
	    {
	      return atoi(buff);
	    }
      }
    }
}

/* itoa:  convert n to characters in s */
void itoa(int n, char s[])
{
    int i, sign;

    if ((sign = n) < 0)  /* record sign */
        n = -n;          /* make n positive */
    i = 0;
    do {       /* generate digits in reverse order */
        s[i++] = n % 10 + '0';   /* get next digit */
    } while ((n /= 10) > 0);     /* delete it */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}

/* reverse:  reverse string s in place */
void reverse(char s[])
{
    int i, j;
    char c;

    for (i = 0, j = strlen(s)-1; i<j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}
