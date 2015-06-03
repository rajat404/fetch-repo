import sys
import requests
url = "https://api.github.com/users/"+sys.argv[1]+"/repos"
req = requests.get(url)
resp = req.json()
repolist = []
with open("repolist-github.txt", 'w+') as f:
	for eachDict in resp:
		f.write("%s\n" % str(eachDict['name']))
