#!/bin/bash

for file in `find ../ -name "*.pyc" -type f`
do
  echo "rm -f ${file}"
  rm -f ${file}
done
