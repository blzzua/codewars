// https://www.codewars.com/kata/576b93db1129fcf2200001e6

using System;
//using System.Linq;

public static class Kata
{
  public static int Sum(int[] numbers)
  {
    if (numbers == null) {return 0;}
    if (numbers.Length < 2) {return 0;}
    
    int[] sorted_numbers = numbers.Clone() as int[];
    Array.Sort(sorted_numbers);
    int res_sum = 0;
    for (int i = 1; i < sorted_numbers.Length - 1; i++)
    {
      res_sum = res_sum + sorted_numbers[i];
    }
    return res_sum;
  }
}