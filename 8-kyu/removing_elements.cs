// https://www.codewars.com/kata/5769b3802ae6f8e4890009d2

using System.Collections.Generic;

public static class Kata
    {
        public static object[] RemoveEveryOther(object[] arr)
        {
            var res = new List<object>();
            for (var i = 0; i < arr.Length; i++){
              if ( i % 2 == 0){
                res.Add(arr[i]);
              }
            }
            return res.ToArray();
        }
    }

// clean arrays
using System.Collections.Generic;
using System;

public static class Kata
    {
        public static object[] RemoveEveryOther(object[] arr)
        {
          int res_len = (arr.Length + 1) / 2;
          object[] res = new object[res_len];

          int res_i = 0;
          for (var i = 0; i < arr.Length; i++){
            if ( i % 2 == 0){
                res[res_i] = arr[i];
                res_i ++;
              }
          }
        
        return res;
        }
    }