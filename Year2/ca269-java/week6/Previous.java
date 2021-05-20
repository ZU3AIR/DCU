import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Previous
{
    public static void main(String [] args)
    {
        Set<Integer> set = new HashSet<Integer>();
        System.out.print("Enter some numbers (-1 to end)");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        while(num != -1){
            set.add(num);
            num = in.nextInt();
        }
        for(int i : set)
            if(set.contains(i)){
                System.out.print(i + " ");
            }
            
    }
}