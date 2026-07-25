#!/bin/bash

: <<Idea
Creating a backup script as a beginner project
Idea

set -euo pipefail

SOURCE_DIR="$HOME/DevOps/Shell-Scripting/Projects/Scripts"
DEST_DIR="$HOME/DevOps/Shell-Scripting/Projects"

if [ ! -d "${SOURCE_DIR}" ]; then
        echo "The ${SOURCE_DIR} directory does not exist."
        exit 1
fi

if [ -z "$(find "${SOURCE_DIR}" -maxdepth 1 -name '*.txt' -print -quit)" ]; then
        echo "No files with .txt extension is found in the ${SOURCE_DIR} directory."
else   
        tar -czvf "${DEST_DIR}/backup_$(date +%Y%m%d).tar.gz" "${SOURCE_DIR}"
        echo "Backup created: ${DEST_DIR}/backup_$(date +%Y%m%d).tar.gz"
fi