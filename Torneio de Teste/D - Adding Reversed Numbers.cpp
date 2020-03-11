#include <iostream>
 
using namespace std;
 
int reverseNumber(int number);

int main() {

    int numCalc;
    scanf("%d", &numCalc);

    int num1, num2, sum;

    for(int i = 0; i < numCalc; i++){
        scanf("%d %d", &num1, &num2);
        num1 = reverseNumber(num1);
        num2 = reverseNumber(num2);
        printf("%d\n", reverseNumber(num1 + num2));
    }
 
    return 0;
}


int reverseNumber(int number){
    int reversedNumber = 0;
    while(number > 0) {
        reversedNumber = (reversedNumber * 10) + (number % 10);
        number /= 10;
    }
    return reversedNumber;
}