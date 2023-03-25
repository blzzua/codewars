# https://www.codewars.com/kata/58305403aeb69a460b00019a

def reverse_and_mirror(s1, s2):
    sep = '@@@'
    def reverse(s):
        return ''.join(s[::-1])
    return reverse(s2).swapcase() + sep + reverse(s1).swapcase() + s1.swapcase()

# also bash solution

#!/bin/bash
V1=$(echo "$2" | rev | tr '[:upper:][:lower:]' '[:lower:][:upper:]')
V2=$(echo "$1" | rev | tr '[:upper:][:lower:]' '[:lower:][:upper:]')
V3=$(echo "$1" | tr '[:upper:][:lower:]' '[:lower:][:upper:]')
SEP="@@@"
echo "${V1}${SEP}${V2}${V3}"
