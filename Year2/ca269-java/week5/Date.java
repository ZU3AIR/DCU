import java.util.Scanner;

public class Date
{
    private int day;
    private int month;
    private int year;
    
    public Date(String s)
    {
        String[] dates = s.split(" ");
        day = Integer.parseInt(dates[0]);
        month = Integer.parseInt(dates[1]);
        year = Integer.parseInt(dates[2]);
    }
    
    public String toString()
    {
        return day + "/" + month + "/" + year;
    }
    
    public Boolean isOnOrAfter(Date newdate)
    {
        return this.day >= newdate.day && this.month >= newdate.month && this.year >= newdate.year;
    }
    
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        String line;
        //creating a new date
        Date latestdate = new Date(in.nextLine());
        while(in.hasNextLine())
        {
           line = in.nextLine();
           if(line.length() != 0)
           {
              Date date = new Date(line);
              if(date.isOnOrAfter(latestdate))
              {
                  latestdate = date;
              }
              
           }

        }
        System.out.println(latestdate); // Print the latest date
    }
}
