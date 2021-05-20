import java.util.Scanner;

public class Reverse {
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        //array declaration
        int[] values;
        //allocate memory
        values = new int[num];
        System.out.print("Enter " + num + " numbers: ");
        for(int i=0; i<values.length;i++)
        {
            int newnum = in.nextInt();
            values[i] = newnum;
        }

        System.out.print("The numbers reversed are:")
        for(int j=num-1; j>=0; j--)
        {
            System.out.print(" " + values[j]);
        }
        System.out.println();

    }
}
