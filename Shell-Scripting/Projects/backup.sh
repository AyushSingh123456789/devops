#!/bin/bash

set -e

# Configuration Variables
# Sets BASE_DIR to the exact folder containing this script (e.g., ~/DevOps)
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$BASE_DIR/source"
DEST_DIR="$BASE_DIR/backups"
LOG_FILE="$BASE_DIR/backup.log"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$DEST_DIR/backup_$TIMESTAMP.tar.gz"

# Error Handling Callback
cleanup_on_failure() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [ERROR] Backup failed unexpectedly on line $1!" | tee -a "$LOG_FILE"
}

trap 'cleanup_on_failure $LINENO' ERR

# Environment Setup
mkdir -p "$SOURCE_DIR" "$DEST_DIR"

if [ ! "$(ls -A "$SOURCE_DIR")" ]; then
    echo "Sample data generated on $TIMESTAMP" > "$SOURCE_DIR/sample_document.txt"
fi

# Pre-Check Validation
if [ ! -d "$SOURCE_DIR" ]; then
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [ERROR] Source directory does not exist." | tee -a "$LOG_FILE"
    exit 1
fi

if [ ! -w "$DEST_DIR" ]; then
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [ERROR] Destination directory is not writable." | tee -a "$LOG_FILE"
    exit 1
fi

# Execution
echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] Starting backup process..." | tee -a "$LOG_FILE"

tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .

echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] Backup successfully created at $BACKUP_FILE" | tee -a "$LOG_FILE"

# Retention (Keep only last 3 backups)
echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] Cleaning up old backups..." | tee -a "$LOG_FILE"
ls -1t "$DEST_DIR"/backup_*.tar.gz 2>/dev/null | tail -n +4 | xargs -r rm -f

echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] Process finished successfully." | tee -a "$LOG_FILE"
