/* fehler.c
 *  
 *  Ein Programm, dass Compilerfehler,
 *  Laufzeitfehler und logische Fehler demonstriert.
 */

#include <stdio.h>

int main() {

  int num1, num2;
  num1 = 0;
  num2 = 1;

  printf("Der Quotient der Variablen ist: ");
  printf("%d\n", num1/num2);
  printf("\n");		   // Leerzeile

  printf("Jetzt werden die Variablenwerte vertauscht.\n");

  // Dies muss korrigiert werden. (logischer Fehler!!!)
    int tmp = num1;
    num1 = num2;
    num2 = tmp;

  printf("Der Quotient der Vaiablen ist nun: ");
  printf("%d\n", num1/num2); // error divison by zero

  return 0;
}
