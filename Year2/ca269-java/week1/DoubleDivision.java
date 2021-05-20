import java.util.Scanner;

public class DoubleDivision {

    public static void main(String [] args)
    {
        System.out.print("Please enter two floating point numbers: ");
        Scanner in = new Scanner(System.in);
        double number1 = in.nextDouble();
        double number2 = in.nextDouble();

        double total = number1 / number2;

        System.out.println(number1 + " / " + number2 + " is " + total);
    }
}
