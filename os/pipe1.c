#include<stdio.h>
#include <unistd.h>

int main(){

int pipe1[2];
int p;
int f;
int n;

printf("Enter number of numbers :");
scanf("%d",&n);
int arr[n];
	
for (int i = 0; i < n; i++) {
    printf("Enter the numbers in the array :");
    scanf("%d", &arr[i]);
}


p = pipe(pipe1);

if (p==-1){
	printf("pipe creation failed");
	return -1;
	}

f=fork();

if (f==-1){
	printf("Fork Failed");
	return -1;
	}	

//child process
if (f==0){
	int numbers[n];
	close(pipe1[1]);
	read(pipe1[0],numbers,n*sizeof(int));
	printf("Numbers received by child : \n");
	for (int i=0;i<n;i++){
	printf("%d\n",numbers[i]);
	}
	
	}
else{
	//Parent Process
	printf("Parent Process ID :%d\n",getpid());
	close(pipe1[0]);
	write(pipe1[1],arr,n*sizeof(int));		
	}

return 0;
}
