# will be run inside docker, no need to run locally
for d in repos/* ; do
    cd "$d"
    pip install library/
    cd ../../
done