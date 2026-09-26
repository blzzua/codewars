// https://www.codewars.com/kata/559d2284b5bb6799e9000047

using System;
  
public class Kata
{
  public static string[] AddLength(string str)
  {
    string[] strArr = str.Split(' ');
    string res = "";
    
    for (int i = 0; i < strArr.Length; i++)
    {
      strArr[i] = $"{strArr[i]} {strArr[i].Length}";
      res = res + strArr[i];
      if (i < strArr.Length - 1){
        res = res + ' ';
      }
      Console.WriteLine(strArr[i]);
    }
    
    return strArr;
  }
}
