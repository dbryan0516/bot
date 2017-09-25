#!/bin/bash
set -e

TIMESTAMP=`date +'%Y-%m-%d %H:%M %Z'`
REPO_DIR=/home/dylan/Desktop/bot/
FILE=transactions.log

FILES_TO_COMMIT=${REPO_DIR}${FILE}

git add ${FILES_TO_COMMIT}
git commit -m "AUTOCOMMIT ${TIMESTAMP}"
git push
