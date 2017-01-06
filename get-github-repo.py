import sys
import os
from getpass import getpass
from github3 import GitHub


def main():
    username = raw_input("Enter username: ")
    password = getpass()
    githubObj = GitHub(username, password)

    ssh_url_list = []
    html_url_list = []

    choice = raw_input("Do you want to clone the repositories of your organization? [Y/N] ")
    if choice == 'y' or choice == 'Y':
        all_repos = githubObj.repositories()
        for repo in all_repos:
            ssh_url_list.append(repo.ssh_url)
            html_url_list.append(repo.html_url)
    else:
        user_repos = githubObj.repositories_by(username)
        for repo in user_repos:
            ssh_url_list.append(repo.ssh_url)
            html_url_list.append(repo.html_url)

    clone_choice = raw_input("Do you want to clone via SSH [Y/N] ")
    if clone_choice == 'y' or clone_choice == 'Y':
        print "Initiating Cloning via SSH"
        for url in ssh_url_list:
            os.system("git clone " + url)

    else:
        print "Initiating Cloning via HTTPS"
        for url in html_url_list:
            os.system("git clone " + url)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print e
        print "\nQuiting..."
        sys.exit(0)
