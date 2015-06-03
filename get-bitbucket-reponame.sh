#!/bin/bash
# Script that gets the list of names of all repositories on Bitbucket
# Usage: get-bitbucket-reponame.sh [username]
# Source: https://movingtothedarkside.wordpress.com/2015/01/10/clone-all-repositories-from-a-user-bitbucket/

curl -u ${1} https://api.bitbucket.org/1.0/users/${1} > repoinfo-bitbucket.txt
for repo_name in `cat repoinfo-bitbucket.txt | sed -r 's/("name": )/\n\1/g' | sed -r 's/"name": "(.*)"/\1/' | sed -e 's/{//' | cut -f1 -d\" | tr '\n' ' '`
do
    echo $repo_name >> repolist-bitbucket.txt
done
