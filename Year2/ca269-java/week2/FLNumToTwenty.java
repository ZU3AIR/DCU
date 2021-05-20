import java.util.Scanner;

public class FLNumToTwenty {
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = in.nextInt();
        for(int i=num; i<=20; i++)
        {
            System.out.print(i + " ");
        }
        System.out.println();
    }    
}
