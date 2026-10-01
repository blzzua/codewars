// https://www.codewars.com/kata/57fae964d80daa229d000126

using System.Text;

public class Kata
{
  public static string Remove(string s)
  {
    StringBuilder sb = new StringBuilder(s);
    if (s[s.Length-1] == '!')
    {
      sb.Remove(sb.Length-1,1);
    }
    return sb.ToString();
  }
}