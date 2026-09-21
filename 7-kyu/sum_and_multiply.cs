// https://www.codewars.com/kata/59971206e06bbf4407002382

public class Kata
{
  public static int[] SumAndMultiply(int sum, int multiply)
  {
    if (System.Math.Pow(sum, 2) < 4 * multiply) {
      return null;
    }
    int D = (int) System.Math.Sqrt( System.Math.Pow(sum, 2) - 4 * multiply );
    int x = (sum - D) / 2;
    int y = (sum + D) / 2;
    if (x + y == sum && x * y == multiply){
        return new[]{x, y};
    }
    return null;
  }
}
