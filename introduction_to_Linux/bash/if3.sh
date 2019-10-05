#!/bin/bash

if [[ -f $1 ]]
then 
  echo "Removing file"
  rm $1
elif [[ -d $1 ]]
then
  echo "Removing dir"
else
  echo "Can't remove $1"
fi
