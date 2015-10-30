git-current-contributors(1) -- List authors that own code in current branch
================================

## SYNOPSIS

`git-current-contributors` [-h] [--path PATH] [-r] [-s]
                                [-i {author,author-mail,committer,commiter-mail}]
                                [-a] [-t TOP_N] [-b] [--self-update] [-v]
                                [--version]

## DESCRIPTION

List authors that own code in current branch

Blame files recursively and calculate how much code belongs to each found
author in current repository stage. This metric will be calculated over
git-ls-files(1) command which ignore .gitignore matches

## OPTIONS

-h, --help
show this help message and exit

--path PATH
A path to be inspected that uses current directory as default

-r, --reverse
Sort in reversed order (can be combined with --alphabetically)

-s, --alphabetically
Sort alphabetically instead sorting by amount

-i {author,author-mail,committer,commiter-mail}, --identifier {author,author-mail,committer,commiter-mail}
Define the key used in parse process for fetching contributors

-a, --show-absolute
Print the absolute number of lines owned

-t TOP_N, --top-n TOP_N
Set max number of contributors for listing. Set -1 to unlimit output

-b, --force-binaries
Run blame over binaries files (not recommended)

--self-update
Update the command itself when updates are available

-v, --verbose
Increase verbosity

--version
Show program's version number and exit

## EXAMPLES

$ git current-contributors --top-n="10" --reverse

## AUTHOR

Written by Moacir Rosa <paulomoacir.junior@gmail.com>

## REPORTING BUGS

&lt;<https://github.com/moacirosa/git-current-contributors/issues>&gt;

## SEE ALSO

&lt;<https://github.com/moacirosa/git-current-contributors>&gt;
