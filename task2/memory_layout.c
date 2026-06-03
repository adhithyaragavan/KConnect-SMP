#include <stdio.h>
#include <unistd.h>

int main(){
	pid_t pid = getpid();
	printf("cat /proc/%d/maps\n", pid);
	sleep(60);
	return 0;


}
