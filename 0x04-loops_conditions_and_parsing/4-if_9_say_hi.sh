#!/usr/bin/env bash
# This script prints "Best School" 10 times using while but prints hy
# after the 9th iteration

count=1

while [ $count -le 11 ]; do

	if [ $count -eq 10 ]; then
		echo "Hi"

	else
		echo "Best School"
	fi

	((count++))
done
