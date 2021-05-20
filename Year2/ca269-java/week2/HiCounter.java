import java.util.Scanner;
public class HiCounter {
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a phrase:: ");
        String word = in.next();
        int counter = 0;
        for(int i=1;i<word.length();i++)
        {
            if(word.substring(i-1,i+1).equals("hi")){
                counter = counter + 1;
            }
        }
        System.out.println(counter);
    }
}
