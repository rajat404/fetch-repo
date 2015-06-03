#!/bin/bash
# Script that reads repo names from `repolist-github.txt` and recursively clones each repo
# Usage: clone-github-repo.sh [username]
for repo_name in `cat repolist-github.txt`
do
    echo "Cloning " $repo_name
    git clone git@github.com:${1}/$repo_name.git
    echo "---"
done
