import java.util.Scanner;

public class Inches2cm
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter a quantity in inches: ");
        
        int number = in.nextInt();
        double conversion = number * 2.54;
        // Find out how many inches (use a whole number for integers)

        // Print out the result
        System.out.println(number + " inch is " + conversion + " cm");
    }   
}