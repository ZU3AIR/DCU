import java.util.Scanner;

public class EvenOdd {
    public static void main(String [] args)
    {
        System.out.print("Enter a number: ");
        Scanner in = new Scanner(System.in);
        int number = in.nextInt();

        if (number % 2 == 0)
        {
            System.out.println(number + " is even.");
        }
        else
        {
            System.out.println(number + " is odd.");
        }
    }

}
