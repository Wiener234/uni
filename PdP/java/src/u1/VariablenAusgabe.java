/** VariablenAusgabe.java
 *
 *  Ein Programm, das die Vereinbarung sowie 
 *  die Ausgabe von Variablen einfacher Datentypen
 *  demonstriert.
 */


class VariablenAusgabe {

  public static void main (String[] args) {

    int num1 = 12;
    int num2 = -4;

    System.out.println(num1);
    System.out.println(num2);
    System.out.println();

    System.out.println(5);
    System.out.println(5 + num2);
    System.out.println();

    System.out.print(5);
    System.out.println(num2);

    System.out.println(num1 + " " + num2);

    System.out.println("Wert von num1: " + num1);


    String sting = "P r o g r a m m";
    System.out.println(sting.substring(1,3));
  }
}

// VariablenAusgabe
