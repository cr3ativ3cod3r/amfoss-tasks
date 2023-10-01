#include<iostream>

int main() {
	int n;
	std::cout<<"n= ";
	std::cin >> n;

	if (n >= 2) {
	    for(int i=2;i<=n+1;i++){
		int a=0;
		for (int j=2;j<=n;j++){
		    if (i%j!=0){
		        a++;
		    }
		}
		if (a==n-2){
		    std::cout<<i<< std::endl;
		}}}
}
