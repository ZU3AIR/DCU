import java.util.Scanner;

public class IsTeenager {
    public static void main(String [] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = input.nextInt();

        switch (age){

            case 13:
            case 14:
            case 15:
            case 16:
            case 17:
            case 19:
                System.out.println("You are a teenager.");
                break;
            default:
                System.out.println("You are not a teenager.");

        } 
    }    
}
