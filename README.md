# Private python repos

Soon in your code you will want to add a private python repo to do that we: 
1. generate an ssh key in our local machine and add that to the github repo
2. then we copy this ssh key in put it in the .ssh file (which is not part of the version controle)
3. the docker containers will not: 
   1. copy that ssh key to the container
   2. use it to pull the private libraries mentioned in the private_libraries.text
   3. after that delete the ssh key again, so it doesnt stick around in the docker containers. 
