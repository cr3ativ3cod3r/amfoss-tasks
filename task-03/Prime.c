#include <stdio.h>


int main(){
    int n;
    printf("n=");
    scanf("%d",&n);
    if (n >= 2) {
	    for(int i=2;i<=n+1;i++){
		int a=0;
		for (int j=2;j<=n;j++){
		    if (i%j!=0){
		        a++;
		    }
		}
		if (a==n-2){
		    printf("%d\n",i);
		}
	    }
    } else {
        printf("There are no prime numbers for n < 2.\n");
    }
    return 0;
}
