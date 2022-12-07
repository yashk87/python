#include <stdio.h>
int main(){
    int count = 0;
    for(int i = 0;i<=4;i++){
        printf("*");
        if(count == 0){
        for(int j = 0;j<=4;j++){
            printf("*");
        }
        count = count+1;
        }
        if(i==4){
           for(int j = 0;j<=4;j++){
            printf("*");
        }
        }
        printf("\n");
    }
}