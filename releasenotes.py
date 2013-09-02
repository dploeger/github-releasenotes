# coding=utf-8
""" Create release notes with the issues from a milestone.
"""

__author__ = 'Dennis Plöger <develop@dieploegers.de>'

import argparse
import urllib2
import json

github_url='https://api.github.com/repos'

if __name__ == '__main__':

    # Parse arguments

    parser = argparse.ArgumentParser(
        description = 'Create a draft release with the issues from a milestone.'
    )

    parser.add_argument(
        'user',
        metavar='user',
        type=str,
        help='github user'
    )

    parser.add_argument(
        'repository',
        metavar='repository',
        type=str,
        help='githb repository'
    )

    parser.add_argument(
        'milestone',
        metavar='name of milestone',
        type=str,
        help='name of used milestone'
    )

    parser.add_argument(
        '-c', '--closed',
        help='Fetch closed milestones/issues',
        action='store_true'
    )

    args = parser.parse_args()

    # Fetch milestone id

    url = "%s/%s/%s/milestones" % (
        github_url,
        args.user,
        args.repository
    )

    if args.closed:
        url += "?state=closed"

    github_request = urllib2.urlopen(url)

    if not github_request:
        parser.error('Cannot read milestone list.')

    decoder = json.JSONDecoder()

    milestones = decoder.decode(github_request.read())

    github_request.close()

    milestone_id = None

    for milestone in milestones:
        if milestone['title'] == args.milestone:
            milestone_id = milestone['number']

    if not milestone_id:

        parser.error('Cannot find milestone')

    url = '%s/%s/%s/issues?milestone=%d' % (
        github_url,
        args.user,
        args.repository,
        milestone_id
    )

    if args.closed:
        url += "&state=closed"

    github_request = urllib2.urlopen(url)

    if not github_request:
        parser.error('Cannot read issue list.')

    issues = decoder.decode(github_request.read())

    github_request.close()

    for issue in issues:

        labels = []

        for label in issue['labels']:
            labels.append(label['name'])

        print ' * #%d - %s [%s]' % (
            issue['number'],
            issue['title'],
            ', '.join(labels)
        )