import java.io.*;

public class SimpleStreamDemo {
    public static void main(String args[]) throws IOException
    {
        System.out.println("Enter characters, and '0' to quit.");
        int tmp;
        do {
            tmp = System.in.read();
            System.out.println(tmp + " : " + (char)tmp);
        } while ((char)tmp != '0');
    }
}
