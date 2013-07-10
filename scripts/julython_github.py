# -*- coding: utf-8 -*-


import argparse
import os

from github import Github


JULYTHON_HOOK_URL = 'http://www.julython.org/api/v1/github'
JULYTHON_HOOK = {
    'name': 'web',
    'config': {
        'url': JULYTHON_HOOK_URL,
        'content_type': 'form'
    },
    'events': ['push'],
    'active': True
}


def ensure_julython_hooks(access_token):
    github = Github(access_token)
    user = github.get_user()
    user_python_repos = [
        repo for repo in user.get_repos()
        if repo.owner.login == user.login
        and repo.language and 'python' in repo.language.lower()
    ]
    for repo in user_python_repos:
        if has_julython(repo):
            print repo.name, 'already has julython!'
        else:
            print 'Adding julython to', repo.name
            repo.create_hook(**JULYTHON_HOOK)


def has_julython(repo):
    for hook in repo.get_hooks():
        if hook.config['url'] == JULYTHON_HOOK_URL:
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("access_token", help="Your personal GitHub API access token. Generate one at: https://github.com/settings/applications")
    args = parser.parse_args()
    access_token = args.access_token
    ensure_julython_hooks(access_token)


if __name__ == '__main__':
    main()
