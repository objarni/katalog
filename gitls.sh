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
ls $WORKDIR
clean_workdir
