// https://www.codewars.com/kata/53dc23c68a0c93699800041d


public class Kata
{
  public static string Smash(string[] words)
  {
    string res = "";
    for (int i = 0 ;  i < words.Length; i++)
    {
      if (i > 0)
      {
        res = res + " ";
      }
      res = res + words[i];
    }
    return res;
  }
}


// String.Join
using System;
res = String.Join(" ", words);
