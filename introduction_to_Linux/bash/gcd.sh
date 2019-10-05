#!/bin/bash

gcd () # n, m
{
  if [[ $1 -eq $2 ]]
  then 
    ans=$1
  elif [[ $1 -lt $2 ]]
  then 
    let "s=$2 - $1"
    gcd $1  $s
  else
    let "s=$1 - $2"
    gcd $s $2
  fi
}

while true
do 
  read -p "" n m
  # echo "$n"
  if [[ "$n" == "" ]]
  then 
    break
  else
    gcd $n $m
    echo "GCD is $ans" 
  fi
done 

echo "bye"

