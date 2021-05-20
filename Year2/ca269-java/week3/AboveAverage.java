//
// Supplied code to help ensure there will be no output formatting issues.
//
import java.util.Scanner;

public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        //array declaration
        double[] array;
        //allocate memory
        array = new double[num];
        
        System.out.print("Enter " + num + " numbers: ");
        double sum = 0;
        for(int i=0;i<num;i++)
        {
            double newnum = in.nextDouble();
            sum = sum + newnum;
            array[i] = newnum;
        }
        double average = sum/num;
        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");
        for(int j=0;j<array.length;j++)
        {
            if(array[j] > average){
                System.out.print(" " + array[j]);        
            }
        }

        System.out.println(); // Should finish with a new line
    }
}