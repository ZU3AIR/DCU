import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class ListSort {
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        List<Integer> values = new ArrayList<Integer>();
        System.out.print("Enter numbers: ");
        int num = in.nextInt();

        while(num != -1)
        {
            values.add(num);
            num = in.nextInt();
        }
    
    Collections.sort(values);
    System.out.print("Sorted: ");

    for(int i : values)
    {
        System.out.print(i + " ");
    }

    }
}
