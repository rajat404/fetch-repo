# fetchRepo
clone/backup all your repositories with a few scripts

One often needs to backup his/her repositories from Bitbucket or Github. This can be a cumbersome and boring process. So this is a simple attempt to allow simple backup of all repositories of a particular user. Currently support for organization repositories is not provided. 

#Usage

* First generate a list of all your repositories by running `get-bitbucket-reponame.sh [username]`
You can also manually write the names of your repositories to the file `repolist.txt`

* Then run `clone-bitbucket-repo.sh [username]`

Et voilà!
