# Private python repos
this is useful if you have private python libraries you want to import to your project. 

# Cookiecutter 

`cookiecutter git@github.com:leanderloew/FDL-starter.git --checkout private_python_libraries`

## What it does
We provide 3 scripts:

1. clone_packages.sh
2. install_packages.sh 
3. update_packages.sh

# Clone
clone_packages.sh will clone your private libraries to the repos folder, this folder gets ignores by git (since your private) libraries
should be handled i their own repo. You will only have to run this at the beginning and whenever you add a new private package

# Install 
After you cloned the libraries, inside the docker file they get copied to the container and then installed inside the 
container. So whenever the files change they will be automatically re-installed. You will never have to run install_packages.sh 
explicitly.

# Update
Whenever you updated one of the libraries externally, you can run update_packages.sh (or cd and run git update inside the folder)