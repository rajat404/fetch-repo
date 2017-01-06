import sys
import os
import requests
from getpass import getpass


def get_val(response):
    html_url_list, ssh_url_list = [], []
    for repo in response['values']:
        for item in repo['links']['clone']:
            if item['name'] == 'https':
                html_url_list.append(item['href'])
            else:
                ssh_url_list.append(item['href'])
    return html_url_list, ssh_url_list


def make_call(url, username, password):
    html_url_list, ssh_url_list = [], []
    req = requests.get(url, auth=(username, password))
    response = req.json()
    if 'next' in response:
        url = response['next']
        temp_html_list, temp_ssh_list = get_val(response)
        html_url_list.extend(temp_html_list)
        ssh_url_list.extend(temp_ssh_list)
        make_call(url, username, password)
    return html_url_list, ssh_url_list


def main():
    username = raw_input("Enter username: ")
    password = getpass()

    ssh_url_list = []
    html_url_list = []

    choice = raw_input(
        "Do you want to clone the repositories of your organization? [Y/N] ")
    if choice == 'y' or choice == 'Y':
        organization = raw_input("Enter the organization name: ")
        url = "https://api.bitbucket.org/2.0/teams/" + \
            organization + "/repositories"
        print "Please wait, this might take a while..."
        html_url_list, ssh_url_list = make_call(url, username, password)
    else:
        # url = "https://bitbucket.org/api/1.0/users/"+username
        url = "https://bitbucket.org/!api/2.0/repositories/" + username
        req = requests.get(url, auth=(username, password))
        response = req.json()
        html_url_list, ssh_url_list = get_val(response)

    clone_choice = raw_input("Do you want to clone via SSH [Y/N] ")
    if clone_choice == 'y' or clone_choice == 'Y':
        print "Initiating Cloning via SSH"
        for url in ssh_url_list:
            os.system("git clone --mirror " + url)

    else:
        print "Initiating Cloning via HTTPS"
        for url in html_url_list:
            os.system("git clone --mirror " + url)


if __name__ == '__main__':
    try:
        main()
    except:
        print "\nQuiting..."
        sys.exit(0)
