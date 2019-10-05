#!/bin/bash

while echo "enter your name:"
do
  read name
  if [[ -n $name ]]
  then
      echo "enter your age:"
      read age
      case $age in
        0) break;;
        [1-9]|1[0-6]) group="child";;
        1[7-9]|2[0-5])  group="youth";;
        *) group="adult"
      esac
    echo "$name, your group is $group"
  else
    break
  fi
done

echo "bye"

