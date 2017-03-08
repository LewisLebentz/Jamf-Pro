import json
import urllib2

url = 'http://omahaproxy.appspot.com/all.json'
resp = urllib2.urlopen(url)


data = json.loads(resp.read())

for each in data:
    if each.get("os") == "mac":
        versions = each.get("versions")
        for version in versions:
            if version.get("channel") == "stable":
                print (version.get("current_version"))
