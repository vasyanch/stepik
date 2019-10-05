#!/bin/bash

calc () # f op s
{
  case $op in  "+" | "-" | "/" | "*" | "%" | "**") let "ans=$f$op$s";;
                *) echo "error"; exit
  esac
  echo "$ans"
}

while true 
do
  read -p "" f op s 
  if [[ $op == "" ]]
  then  
    case $f in 
      "exit") echo "bye"; exit;; 
      *) echo "error"; exit
    esac
  else 
    case $s in
      "") echo "error"; exit;;
      *) calc ${f} ${op} ${s}
  esac
  fi
done

