// https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69

using System;

public class Hamming
{
    public static int Distance(string a, string b)
    {
    int l = a.Length;
    int res = 0;
	for (int i = 0; i < l; i++)
    {
      if (a[i] != b[i])
      {
        res++ ;
      };
    }
    return res;
    }
}
