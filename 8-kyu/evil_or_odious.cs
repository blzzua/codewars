// https://www.codewars.com/kata/56fcfad9c7e1fa2472000034

public class Kata
{
  public static string Evil(int n)
  {
    int local_n = n;
    int res = 0;
    while (local_n > 0) 
    {
      res += local_n % 2;
      local_n = local_n >> 1;
    }
    if (res % 2 ==0){
      return "It's Evil!";
    }
    else
    {
      return "It's Odious!";
    }
  }
}
