import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class EvenOdd
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter numbers: ");

        // making the lists
        List<Integer> oddnumbers = new ArrayList <Integer>();
        List<Integer> evennumbers = new ArrayList <Integer>();
                
        int num = in.nextInt();
        while(num != -1)
        {
            if(num % 2 == 0)
            {
                evennumbers.add(num);
            }
            else{
                oddnumbers.add(num);
            }
            num = in.nextInt();
        }
        System.out.print("Odd:");
        for(int i : oddnumbers)
        {
            System.out.print(" " + i);
        }
        System.out.println();
        System.out.print("Even:");
        for(int i : evennumbers)
        {
            System.out.print(" " + i);
        }
    }
}