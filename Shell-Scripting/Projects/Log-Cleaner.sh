#!/usr/bin/env bash


<< Info
This a Log Cleaner, which is used for cleaning .log files, which have been present on this system for more than 1 year.
Info

set -euo pipefail

LOG_DIR="./logs"
LOG_GLOB="*.log"
DAYS_OLD=30

TARGET_DIR="$(cd "$LOG_DIR" 2>/dev/null && pwd || true)"

if [[ -z "${TARGET_DIR}" || ! -d "${TARGET_DIR}" ]]; then
	echo "ERROR: Target directory '$LOG_DIR' does not exist. Aborting."
	exit 1
fi

echo "Cleaning log files older than ${DAYS_OLD} days in: ${TARGET_DIR}"

echo #blank space line

find "$TARGET_DIR" -type f -name "$LOG_GLOB" -mtime + "$DAYS_OLD" - 
print -delete

echo # blank space line
echo "Done."
