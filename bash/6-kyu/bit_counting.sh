#!/bin/bash
# https://www.codewars.com/kata/526571aae218b8ee490006f4

n=$1
res_cnt=0
while [[ $n -ne 0 ]];
do
  res_cnt=$((res_cnt + (n%2) ))
  n=$((n/2))
done
echo -n $res_cnt
