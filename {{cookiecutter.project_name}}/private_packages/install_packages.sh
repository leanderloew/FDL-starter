for d in repos/* ; do
    cd "$d"
    pip install library/
    cd ../../
done