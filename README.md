# Git Current Contributors

It's a custom _Git subcommand_ that attempts to answer a question: **"How much code I've wrote is STILL there?"** Maybe it's just a dummy metric but it's fun :)

## Install

_(to be done)_
_Put in your system (Linux, MacOS) PATH and use like custom git commands_

## Usage

Just grabbing some repository and running the command:

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

In example above verbosity was increased showing absolute number of lines currently "owned"

```shell
$ git current-contributors -h

# usage: git-current-contributors [-h] [--path PATH]
#                                 [-i # {author,author-mail,committer,commiter-mail}]
#                                 [-v] [--version]
#
# A custom Git command
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --path PATH           A path to be inspected that uses current directory as
#                         default
#   -i {author,author-mail,committer,commiter-mail}, --identifier {author,author-mail,committer,commiter-mail}
#                         Define the key used in parse process for fetching
#                         contributors
#   -v, --verbose         Increase verbosity
#   --version             show program's version number and exit
```

...and complete usage information

## Author

Moacir Rosa - paulomoacir.junior@gmail.com - http://twitter.com/moacirosa<br/>
See also the list of [contributors](https://github.com/moacirosa/git-current-contributors/graphs/contributors) which participated in this project.

## License

**git-current-contributors** is licensed under the MIT License - see the [LICENSE](https://github.com/moacirosa/git-current-contributors/blob/master/LICENSE) for details
