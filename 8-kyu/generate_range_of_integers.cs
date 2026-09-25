# https://www.codewars.com/kata/55eca815d0d20962e1000106

public class Kata
{
  public static int[] GenerateRange(int min, int max, int step)
  {
    int count = (int)System.Math.Floor((double)(max - min) / step) + 1;
    int[] res = new int[count];
    int res_index = 0;
    
    for (int i = min; i <= max; i = i + step) {
      res[res_index] = i;
      res_index++;
    }
    
    return res;
  }
}
