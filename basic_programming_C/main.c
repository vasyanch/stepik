#include <stdio.h>
#include <stdlib.h>

int f(int i){
    if (i == 1){
        return 1;
    }
    return i * f(i-1);
}

int main() {
    //printf("Hello, World!\n");
/*
    int a=3, b=4;
    double res = 0.75;

    printf("||-----|-----|-----|-----||\n");
    printf("|| act | one | two | res ||\n");
    printf("||=====+=====+=====+=====||\n");
    printf("||%5c|%-5d|%-5d|%5.5d||\n",'+',a,b,a+b);
    printf("||%5c|%5d|%5d|%5.4d||\n",'-',a,b,a-b);
    printf("||%5c|%5d|%-5d|%5.5d||\n",'*',a,b,a*b);
    printf("||%-5c|%-5d|%5d|%5.3f||\n",'/',a,b,res);
    printf("===========================");
*/

/*
    int a, b, res;

    scanf("%d", &a); // считываем целое значение в переменную a
    scanf("%d", &b); // считываем целое значение в переменную b

    res = a + b;
    printf("%d + %d = %d\n", a, b, res);
*/

/*

    int age, height, weight;
    double bov_m, bov_f;

    printf("Vash vozrast?(god)\n");
    scanf("%d", &age); // считываем целое значение в переменную age

    printf("Vash rost?(cm)\n");
    scanf("%d", &height); // считываем  значение в переменную height

    printf("Vash ves?(kg)\n");
    scanf("%d", &weight); // считываем значение в переменную weight

    bov_m = 10*weight + 6.25*height - 5*age + 5;
    bov_f = 10*weight + 6.25*height - 5*age - 161;
    printf("|       BMR       |\n");
    printf("|  male  | female |\n");
    printf("|%8.2f|%8.2f|\n",bov_m, bov_f);27
*/

/*
    int dollars;
    double kurs, rub;
    scanf("%d %lf", &dollars, &kurs);
    rub = dollars * kurs;
    printf("%lf\n", rub);
*/

/*
    printf("%.5lf\n", (1 + 1.0/f(1) + 1.0/f(2) + 1.0/f(3)));
    printf("%.5lf\n", (1 + 1.0/f(1) + 1.0/f(2) + 1.0/f(3) + 1.0/f(4)));
    printf("%.5lf\n", (1 + 1.0/f(1) + 1.0/f(2) + 1.0/f(3) + 1.0/f(4) + 1.0/f(5)));
*/

    char k = 0;

    for(int i = 0; i < 255; i++){
        k = i;
        printf("%c = %d\n", k, k);
    }



    return 0;
}