# Git Current Contributors

It's a custom _Git subcommand_ that attempts to answer a question: **"How much code I have written and is STILL there?"** Maybe it's just a dummy metric but it's fun :)

## Install

Install consists in adding [git-current-contributors](https://github.com/moacirosa/git-current-contributors/blob/master/git-current-contributors) file to your $PATH. There are a lot of ways of doing that. If you trust me here it follow a suggestion:

```shell
  $ curl -sS https://raw.githubusercontent.com/moacirosa/git-current-contributors/master/install | bash
```

> **Note:** Run a new shell session or run `source ~/.bashrc` if you can't

You can check if everything is fine running `git help -a`:

```
...
git commands available from elsewhere on your $PATH

  current-contributors

'git help -a' and 'git help -g' lists available subcommands and some
...
```

### Requirements

- Unix, MacOS
- Python2+
- Git

## Usage

Just grab some repository and run the custom command:

```shell

$ git clone https://github.com/Seldaek/monolog.git
$ cd monolog
$ git current-contributors

#   2.29% Florian Plattner
#   2.69% barbushin
#   2.79% skymeyer
#   9.09% Christophe Coevoet
#  32.41% Jordi Boggiano
```

...or specifically within a `tests` subfolder:

```shell
$ git current-contributors -v --path="tests"

#  3.25% barbushin (266)
#  3.45% Florian Plattner (282)
#  3.80% skymeyer (311)
#  9.47% Christophe Coevoet (775)
# 27.58% Jordi Boggiano (2256)
```

In example above verbosity was increased by showing absolute number of lines are currently "owned"

```shell
$ git current-contributors -h

#
# usage: git-current-contributors [-h] [--path PATH] [-r] [-a]
#                                [-i {author,author-mail,committer,commiter-mail}]
#                                [-v] [--version]
#
# A custom Git command
#
# optional arguments:
#  -h, --help            show this help message and exit
#  --path PATH           A path to be inspected that uses current directory as
#                        default
#  -r, --reverse         Sort in reversed order (can be combined with
#                        --alphabetically)
#  -a, --alphabetically  Sort alphabetically instead sorting by amount
#  -i {author,author-mail,committer,commiter-mail}, --identifier {author,author-mail,committer,commiter-mail}
#                        Define the key used in parse process for fetching
#                        contributors
#  -v, --verbose         Increase verbosity
#  --version             show program's version number and exit
```

...and complete usage information

## Author

Moacir Rosa - paulomoacir.junior@gmail.com - http://twitter.com/moacirosa<br/>
See also the list of [contributors](https://github.com/moacirosa/git-current-contributors/graphs/contributors) which participated in this project.

## License

**git-current-contributors** is licensed under the MIT License - see the [LICENSE](https://github.com/moacirosa/git-current-contributors/blob/master/LICENSE) for details
