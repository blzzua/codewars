// https://www.codewars.com/kata/568d0dd208ee69389d000016

public class RentalCar {
    
    public static int RentalCarCost(int d) {
       int res = d * 40;
       if (d>6) 
       {
         res = res - 50;
       }
       else if (d>2) 
       {
         res = res - 20;
       }
       return res;
    }
}
