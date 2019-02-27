
import stashy
import sys
import os


stash = stashy.connect("https://stash.**.co.uk/", "", "")
pro = stash.projects.list()

vod  = stash.projects['**'].repos.list()
    
for repo in vod:
    for link in repo['links']['clone']:
        if link['name'] == 'http':
            os.system("git clone %s" % link['href'])
            break