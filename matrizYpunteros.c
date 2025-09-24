#include <stdio.h>

int main(){
    char myNums[4] = {1,2,3,4};
    int i;
    int length = sizeof(myNums)/sizeof(myNums[0]);

    for (i = 0; i < length; i++) {
        printf("%p\n",&myNums);
    }
    return 0;
}