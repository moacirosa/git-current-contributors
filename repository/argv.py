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
    '-s',
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

parser.add_argument(
    '-a',
    '--show-absolute',
    action='store_true',
    default=False,
    help='Print the absolute number of lines owned'
)

parser.add_argument(
    '-t',
    '--top-n',
    type=int,
    default='25',
    help='Set max number of contributors for listing. Set -1 to unlimit output'
)

parser.add_argument(
    '--csv',
    action='store_true',
    default=False,
    help='Print the output in CSV format'
)

parser.add_argument(
    '-b',
    '--force-binaries',
    action='store_true',
    default=False,
    help='Run blame over binaries files (not recommended)'
)

# parser.add_argument(
#     '--no-cache',
#     default=0,
#     action='store_true',
#     help='Avoid using cached info and force parsing repository')
#

parser.add_argument(
     '--self-update',
     default=0,
     action='store_true',
     help='Update the command itself when updates are available')

parser.add_argument(
    '-v',
    '--verbose',
    default=0,
    action='count',
    help='Increase verbosity')

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s 0.5.0')

args = parser.parse_args()
