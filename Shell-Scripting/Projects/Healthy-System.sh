#!/bin/bash

<< Info
This is a basic shell script that tells you about the health of your system, based off 3 readings,
i) Free Memory, ii) CPU state, iii) Disk space.
Info

echo "------------------------------------Welcome to the Facility of System HealthCare-----------------------------------"

echo "" #blank space line 

echo "In this Clinic, we have the facility to check on these 3 necessities of your system, among which you have the power to check all three, but one by one: i) Free Memory in your System, ii) State of your CPU, iii) Vacant Disk Space."

echo "" #blank space line

read -p "Choose any integer from the following Options: 1) Free Memory(free -h), 2) CPU State(top -b -n 1 OR uptime), 3) Disk Space(df -h): " choice1

echo "" #blank space line

if [ "$choice1" == 1 ]; then
	echo "---Running Free Memory stats---"
	echo "$(free -h)"

elif [ "$choice1" == 2 ]; then
	if [ $((RANDOM % 2)) -eq 0 ]; then
		echo "---Running CPU Snapshot (top -b -n 1)---"
		top -b -n 1
	else
		echo "---Running System Load Summary(uptime)---"
		uptime
	fi

elif [ "$choice1" == 3 ]; then
	echo "---Running Disk Space Details---"
	echo "$(df -h)"

else
	echo "Invalid choice of integer value. Try again."
	echo "" #blank space line
fi

echo "" #blank space line

echo "--------------------------------------Thanks for Visiting----------------------------------------------------"

