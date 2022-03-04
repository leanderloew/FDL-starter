for d in repos/* ; do
    cd "$d"
    git pull
    cd ../../
done