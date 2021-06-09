#!/usr/bin/env bash
#
# Lists the root folder of given git repo, which
# is given in argument 1 to script

WORKDIR=/tmp/gitls

clone() {
    # Git clones URL specified in $1
    git clone $1 $2
}

clean_workdir() {
    echo "Cleaning out $WORKDIR"
    rm -rf $WORKDIR
    mkdir -p $WORKDIR
}

clean_workdir
clone $1 $WORKDIR
echo "*** The root content of repo is ***"
ls $WORKDIR
clean_workdir
