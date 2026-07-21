#!/bin/bash

: << Practice
Making a log cleaner with no help of AI at all.
Practice

set -euo pipefail

USER_DIR="$HOME/DevOps/Shell-Scripting/Projects/log"
DAYS=30

if [ ! -d "${USER_DIR}" ]; then
	echo "The ${USER_DIR} not found."
	exit 1
fi

if [ -z "$(find "${USER_DIR}" -maxdepth 1 -name '*.log' -mtime +"${DAYS}" -print -quit)" ]; then
	echo "The ${USER_DIR} directory does not contain any log file present for over ${DAYS} days."
else
	echo "Log file found, deleting it..."
	find "${USER_DIR}" -maxdepth 1 -name '*.log' -mtime +"${DAYS}" -exec rm -f "{}" +
	echo "Deleted the file."
fi
      	
