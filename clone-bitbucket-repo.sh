#!/bin/bash
# Script that reads repo names from `repolist.txt` and recursively clones each repo
# Usage: clone-bitbucket-repo.sh [username]
for repo_name in `cat repolist.txt`
do
    echo "Cloning " $repo_name
    git clone git@bitbucket.org:${1}/$repo_name.git
    echo "---"
done
