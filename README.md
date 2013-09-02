github-releasenotes
===================

Create release notes with the issues from a milestone.

Usage
-----

usage: releasenotes.py [-h] [-c] user repository name of milestone

Create a draft release with the issues from a milestone.

positional arguments:
  user               github user
  repository         githb repository
  name of milestone  name of used milestone

optional arguments:
  -h, --help         show this help message and exit
  -c, --closed       Fetch closed milestones/issues

Example
-------

python releasenotes.py -c octocat octophon v4.0

Will create a list of closed issues within the milestone "v4.0" for the
repository octocat/octophon like this:

 * #2 - Fix typo in awesome.py [bug]
 * #1 - Make something awesome! [improvement]