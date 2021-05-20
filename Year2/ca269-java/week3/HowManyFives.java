public class HowManyFives {
    static int countFives(int[] num)
    {
        count = 0
        for(int i=0;i<num.length;i++)
        {
            if(num[i] == 5)
            {
                count = count + 1;
            }
        }
        return count;
    }
}
