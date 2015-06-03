import sys
import requests
import getpass
username = sys.argv[1]
url = "https://api.github.com/users/"+username+"/repos"
password = getpass.getpass()
req = requests.get(url, auth=(username, password))
resp = req.json()
repolist = []
with open("repolist-github.txt", 'w+') as f:
	for eachDict in resp:
		f.write("%s\n" % str(eachDict['name']))
