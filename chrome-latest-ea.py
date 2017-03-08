#!/usr/bin/python
import json
import urllib2
import os.path
import plistlib

url = 'http://omahaproxy.appspot.com/all.json'
resp = urllib2.urlopen(url)


data = json.loads(resp.read())

for each in data:
    if each.get("os") == "mac":
        versions = each.get("versions")
        for version in versions:
            if version.get("channel") == "stable":
                latest = (version.get("current_version"))
                print latest

print os.path.exists("/Applications/Google Chrome.app")

plistloc = "/Applications/Google Chrome.app/Contents/Info.plist"

pl = plistlib.readPlist(plistloc)
pver = pl["CFBundleShortVersionString"]
print pver

if latest == pver:
        print "<result>Latest</result>"

else:
        print "<result>Old</result>"
