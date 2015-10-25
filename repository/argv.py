import argparse
import re

parser = argparse.ArgumentParser(description="A custom Git command")

parser.add_argument(
    '--path',
    default='',
    help='A path to be inspected that uses current directory as default')

parser.add_argument(
    '-r',
    '--reverse',
    action='store_true',
    help='Sort in reversed order (can be combined with --alphabetically)')

parser.add_argument(
    '-a',
    '--alphabetically',
    action='store_true',
    help='Sort alphabetically instead sorting by amount')

parser.add_argument(
    '-i',
    '--identifier',
    choices=['author', 'author-mail', 'committer', 'commiter-mail'],
    default='author',
    help='Define the key used in parse process for fetching contributors'
)

# parser.add_argument(
#     '--no-cache',
#     default=0,
#     action='store_true',
#     help='Avoid using cached info and force parsing repository')
#
# parser.add_argument(
#     '--self-update',
#     default=0,
#     action='store_true',
#     help='Update the command itself when updates are available')

parser.add_argument(
    '-v',
    '--verbose',
    default=0,
    action='count',
    help='Increase verbosity')

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s 0.1.0')

args = parser.parse_args()
