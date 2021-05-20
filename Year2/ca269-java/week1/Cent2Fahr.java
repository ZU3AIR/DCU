import java.util.Scanner;

public class Cent2Fahr {
    
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        int number = in.nextInt();
        
        double total = (number * 1.8) + 32;

        System.out.println(number + " " + total);
    }
}
