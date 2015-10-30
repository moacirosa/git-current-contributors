# Git Current Contributors

1. [About](#about)
1. [Install](#install)
1. [Usage](#usage)
1. [Options Reference](#options-reference)
1. [Other custom Git commands](#other-custom-git-commands)
1. [License](#license)

## About

It's a custom _Git subcommand_ that attempts to answer a question: **"How much code I have written and is STILL there?"** Maybe it's just a dummy metric but it's fun :)

### Cases

Let's take **[rails/rails](https://github.com/rails/rails)** repository as an
example. [At the moment I'm writing this text](https://github.com/rails/rails/commit/61205422bad5f57111d7e9dc4cfb252908878b95) **[@dhh](https://github.com/dhh)** appears in second place in [top contributors list](https://github.com/rails/rails/graphs/contributors). It makes totally sense since he has contributed a lot a long last years. But... How much of the code produced by him is STILL there? Well... At this moment his only in fourth place and owns **4.38%** of
the entire code.

``` shell
$ git current-contributors -t 10

# 5.25% Aaron Patterson
# 5.03% Rafael Mendonça França
# 4.44% José Valim
# 4.38% David Heinemeier Hansson *
# 4.25% Xavier Noria
# 3.71% Jeremy Kemper
# 3.17% Yves Senn
# 3.09% Sean Griffin
# 3.06% Pratik Naik
# 2.99% Andrew White
```

Or in [linux/kernel](https://github.com/torvalds/linux) repository where **[Mr. Linus Torvalds](https://github.com/torvalds)** appears in 26th place
in [top contributors list](https://github.com/torvalds/linux/graphs/contributors). However [in the moment I'm writing this text](https://github.com/torvalds/linux/tree/8a28d67457b613258aa0578ccece206d166f2b9f)
he owns **15%** of the (current) _entire code_. If you think is not too much he owns _~3 million_ lines of code while the second place owns about 0.5 million.

``` shell
$ git current-contributors -t 10 -a

# 15.00% Linus Torvalds (3.000.000)
# 2.00%  Some Great Developer (500.000)

Note: fix these values as soon as the script runs again :)
```

> **Note:** It took about 24hs running but I was curious about it

## Install

Install consists in adding _[git-current-contributors](https://github.com/moacirosa/git-current-contributors/blob/master/git-current-contributors)_ file to your $PATH. There are a lot of ways of doing this but if you trust me here it follows a suggestion:

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

# 29.95% Jordi Boggian
#  9.36% Christophe Coevoet
#  2.85% skymeyer
#  2.69% barbushin
#  2.32% Florian Plattner
#  (...)

```

... or specifically within a `tests` subfolder:

```shell
$ git current-contributors --path="tests"

# 26.85% Jordi Boggiano
#  9.37% Christophe Coevoet
#  3.85% skymeyer
#  3.43% Florian Plattner
#  3.23% barbushin

```

... or listing top 3 contributors in ASC order showing absolute number of lines:

``` shell
$ git clone https://github.com/lodash/lodash.git
$ cd lodash
$ git current-contributors --top-n="3" --reverse --show-absolute

#  0.15% Xotic750 (174)
#  9.48% jdalton (11323)
# 89.49% John-David Dalton (106933)

```

... or sorting first ten contributors by name:

``` shell
$ git current-contributors --top-n="10" --alphabetically

#  0.10% Graeme Yeates
#  9.48% jdalton
# 89.49% John-David Dalton
#  0.05% Justin Ridgewell
#  0.10% Mathias Bynens
#  0.08% Michał Lipiński
#  0.05% Milos Zivadinovic
#  0.05% octref
#  0.06% Ray Hammond
#  0.15% Xotic750
```

... or showing _mail address_ of top five contributors:

``` shell
$ git current-contributors --top-n="5" --identifier="author-mail"

# 98.96% <john.david.dalton@gmail.com>
#  0.15% <xotic750@gmail>
#  0.10% <yeatesgraeme@gmail.com>
#  0.10% <mathias@qiwi.be>
#  0.08% <michal.lipinski@cgmpolska.pl>
```

## Options Reference

**-h, --help** <br>
_show this help message and exit_

**--path PATH** <br>
_A path to be inspected that uses current directory as default_

**-r, --reverse** <br>
_Sort in reversed order (can be combined with --alphabetically)_

**-s, --alphabetically** <br>
_Sort alphabetically instead sorting by amount_

**-i {author,author-mail,committer,commiter-mail},** <br>
**--identifier {author,author-mail,committer,commiter-mail}** <br>
_Define the key used in parse process for fetching contributors_

**-a, --show-absolute** <br>
_Print the absolute number of lines owned_

**-t TOP_N, --top-n TOP_N** <br>
_Set max number of contributors for listing. Set -1 to unlimit output_

**-b, --force-binaries** <br>
_Run blame over binaries files (not recommended)_

**--self-update** <br>
_Update the command itself when updates are available_

**-v, --verbose** <br>
_Increase verbosity_

**--version** <br>
_Show program's version number and exit_

## Other custom Git commands

- [tj/git-extras](https://github.com/tj/git-extras) GIT utilities -- repo summary, repl, changelog population, author commit percentages and more

> **Note:** Some of them like Git Extra was used as reference during
development of this one

## Author

Moacir Rosa - paulomoacir.junior@gmail.com - http://twitter.com/moacirosa<br/>
See also the list of [contributors](https://github.com/moacirosa/git-current-contributors/graphs/contributors) which participated in this project.

## License

The content of this project itself is licensed under the [Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US), and the underlying source code used to format and display that content is licensed under the [MIT license](https://github.com/moacirosa/git-current-contributors/blob/master/LICENSE).
