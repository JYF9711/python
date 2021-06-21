#include <stdio.h>

int main()
{

	int  book[1001],i,j,k,n;
	scanf("%d",&n);
	
	for (i=0;i<=1000;i++){
		book[i]=0;
	}
	for (i=1;i<=n;i++){
		scanf("%d",&k);
		book[k]++;
	}
	for (i=0;i<=1000;i++){
		for (j=1;j<=book[i];j++){
			printf("%d",i);
		}
	}
	return 0;
}
