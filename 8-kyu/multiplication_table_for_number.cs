// https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce

using System;
using System.Text;


public static class Kata
{
    public static string MultiTable(int number)
    {
        StringBuilder sb = new StringBuilder("");
        for (int i = 1; i <= 10; i++)
        {
          sb.AppendFormat("{0} * {1} = {2}", i, number, i *number);
          if (i < 10) { sb.AppendLine();} 
        }
      string result = sb.ToString();
      return result;
    }
}





// join('\',)

using System;
using System.Text;

public static class Kata
{
    public static string MultiTable(int number)
    {
        string[] lines = new string[10];
        for (int i = 1; i <= 10; i++)
        {
            lines[i - 1] = $"{i} * {number} = {i * number}";
        }
        return String.Join("\n", lines);
    }
}


/// linq 
using System;
using System.Linq;

public static class Kata
{
    public static string MultiTable(int number)
    {
        return String.Join("\n", Enumerable.Range(1, 10)
            .Select(i => $"{i} * {number} = {i * number}"));
    }
}


// dynamic array List + String.Join("\n", .. )

using System;
using System.Collections.Generic;

public static class Kata
{
    public static string MultiTable(int number)
    {
        var lines = new List<string>();
        for (int i = 1; i <= 10; i++)
        {
            lines.Add($"{i} * {number} = {i * number}");
        }
        return String.Join("\n", lines);
    }
}
