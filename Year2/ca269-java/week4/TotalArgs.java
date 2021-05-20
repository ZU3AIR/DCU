public class TotalArgs {
    public static void main(String [] args)
    {
        int total = 0;
        for(int i=0; i<args.length;i++)
        {
            int convertedInt = Integer.valueOf(args[i]);
            total = total + convertedInt;
        }
        System.out.println("The sum of all the args is " + total + ".");
    }
}
