#!/usr/bin/env python
import requests
import json

def run(category, settings):
    print 'Churning...'
    repos = get_repos()
    base_url = 'https://api.github.com/repos/'
    headers = { 'Authorization': 'token ' + settings['github_access_token'] }
    data = get_data()

    for repo in repos:
        if category == repo['category'] or category == 'all':
            url = base_url + repo['owner'] + '/' + repo['name'] + '/issues'
            r = requests.post(url, headers=headers, data=data)
            if r.status_code != 201:
                print 'ERROR: Could not create issue'
                print repo['owner'] + '/' + repo['name']
                print r.status_code
                print r.text
                print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    print 'Congratulations! Your issues have been created. :stork:'

def get_data():
    try:
        title = ''
        body = ''
        with open('issue.txt') as issue:
            for index,line in enumerate(issue):
                if index == 0:
                    title = line.replace('\n', '')
                else:
                    body += line
        data = {
          'title': title,
          'body': body
        }
        return json.dumps(data)
    except:
        print 'Error loading issue.txt'
        sys.exit()

def get_repos():
    try:
        with open('repos.json') as data_file:    
            repos = json.load(data_file)
        return repos
    except:
        print 'Error loading repos.json'
        sys.exit()
