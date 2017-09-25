#!/bin/bash
set -e

TIMESTAMP=`date +'%Y-%m-%d %H:%M %Z'`
REPO_DIR=/home/dylan/Desktop/bot
FILE=transactions.log
GIT=/usr/bin/git

cd ${REPO_DIR} && ${GIT} add ${FILE}
cd ${REPO_DIR} && ${GIT} commit -m "AUTOCOMMIT ${TIMESTAMP}"
cd ${REPO_DIR} && ${GIT} push
