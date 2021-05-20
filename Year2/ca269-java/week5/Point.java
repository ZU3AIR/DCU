public class Point
{
   private double x;
   private double y;

   public Point(double newX, double newY)
   {
      x = newX;
      y = newY;
   }
   
   public Point midPoint(Point point2){
       return new Point((this.x + point2.x)/2,(this.y + point2.y)/2);
   }

   public String toString()
   {
      return "(" + x + ", " + y + ")";
   }
}