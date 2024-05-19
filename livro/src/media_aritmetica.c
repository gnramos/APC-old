#include <stdio.h>

int main(void) {
    float nota_1, nota_2, nota_3, nota_4;
    scanf("%f%f%f%f", &nota_1, &nota_2, &nota_3, &nota_4);
    printf("A média é %f\n", (nota_1 + nota_2 + nota_3 + nota_4) / 4);
    return 0;
}