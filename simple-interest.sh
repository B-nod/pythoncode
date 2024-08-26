#!/bin/bash

# This script calculates simple interest

echo "Enter the principal amount:"
read principal

echo "Enter the rate of interest (in %):"
read rate

echo "Enter the time period (in years):"
read time

# Simple Interest formula: (Principal * Rate * Time) / 100
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo "The Simple Interest is: $interest"
