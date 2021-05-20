public class ReverseArgs {
    public static void main(String [] args)
    {
        int i = args.length - 1;
        while(i>=0)
        {
            System.out.println("args[" + i + "] = " + args[i]);
            i--;
        }
    }    
}
