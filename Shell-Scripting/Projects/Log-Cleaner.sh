#!/usr/bin/env bash


<< Info
This a Log Cleaner, which will allow one to clean all the .log files which have been longer than a fixed number of days.
Info

set -euo pipefail

LOG_DIR="$HOME/DevOps/Shell-Scripting/Projects/logs"
DAYS=30

# Code if the directory doesn't exist:

if [ ! -d "${LOG_DIR}" ]; then
	echo "Error: Directory ${LOG_DIR} does not exist."
	exit 1
fi

echo "Searching for .log files, older than ${DAYS} days in ${LOG_DIR}."

: << 'CodeBelow'
 if empty(-z), the founded directory("$(find ${LOG_DIR})) which is not more than 1(-maxdepth 1), ending with .log extension(-name '*.log'), living for over 30 days(-mtime +${DAYS}), record it(-print), and quit to the next line of code(-quit)
CodeBelow

if [ -z "$(find "${LOG_DIR}" -maxdepth 1 -name '*.log' -mtime +"${DAYS}" -print -quit)" ]; then
	echo "No Log files older than ${DAYS} days in the ${LOG_DIR} directory"
else
	echo "Log file/s older than ${DAYS} days found, deleting it right now..."
	find "${LOG_DIR}" -maxdepth 1 -name '*.log' -mtime +"${DAYS}" -exec rm -f "{}" +
	echo "Cleanup Complete"
fi
