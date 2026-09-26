// https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b

using System.Collections.Generic;

public class Kata
{
  public static List<int> ReverseList(List<int> list)
  {
    List<int> res = new List<int>();
    for (int i  = list.Count - 1; i >= 0; i--){
      res.Add(list[i]);
    }
    return res;
  }
}


/*

  public static List<int> ReverseList(List<int> list)
  {
    var res = new List<int>(list);
    reverse.Reverse();
    return res;
  }

*/
