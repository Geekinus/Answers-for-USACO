/*
PROG: ride
LANG: C
*/

#include<stdio.h>
#include <stdlib.h>

int calculate(char *);

int main()
{
	char CometNumber[10], GroupNumber[10];
	FILE * fin, * fout;

	fin = fopen("ride.in", "r");
	fscanf(fin, "%s", CometNumber);
	fscanf(fin, "%s", GroupNumber);
	fclose(fin);

	fout = fopen("ride.out", "w");

	if (calculate(CometNumber) % 47 == calculate(GroupNumber) % 47)
		fprintf(fout, "%s\n", "GO");
	else
		fprintf(fout, "%s\n", "STAY");
	
	fclose(fout);
	
	return 0;
}

int calculate(char * Number)
{
	int i = 0, multification = 1;
	while(*(Number + i) != '\0')
	{
		multification *= (*(Number + i) - 'A' + 1);
		++i;
	}

	return multification;
}
