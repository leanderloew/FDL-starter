# Private python repos
this is useful if you have private python libraries you want to import to your project. 
## what it does 
1. generate an ssh key in our local machine and add that to the github repo
2. then we copy this ssh key in put it in the .ssh file (which is not part of the version controle)
3. the docker containers will not: 
   1. copy that ssh key to the container
   2. use it to pull the private libraries mentioned in the private_libraries.text
   3. after that delete the ssh key again, so it doesnt stick around in the docker containers. 
4. the url has to have the form 
git+ssh://git@github.com/YOUR_REPO_URL_FOR_SSH#subdirectory=SUBDIRECTOY_WHERE_THE_SETUP,PY_IS

## Tips
you might get a permission error in your id_rsa file you can run 
```
chmod 400 ~/.ssh/id_rsa
```
to fix it. 
