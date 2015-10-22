import os
import re
import subprocess
from collections import Counter

class RepositoryAnalyser:

    def __init__(self, repository_path, verbosity=0):
        self.repository_path = repository_path
        self.verbosity = verbosity

    def get_files(self, path = ''):

        os.chdir(self.repository_path)

        parameters = ['git', 'ls-files', path]
        files = subprocess.check_output(parameters, universal_newlines=True)

        return files.split()

    def blame(self, file, skip_binary = True):

        os.chdir(self.repository_path)

        if self.is_binary(file) and skip_binary:

            if self.verbosity > 2:
                print('Skipping (binary) {} ...'.format(file))

            return ''

        if self.verbosity > 2:
            print('Running over {} ...'.format(file))

        parameters = ['git', 'blame', '--line-porcelain', '-w', file]
        blame = subprocess.check_output(parameters, universal_newlines=True)

        return blame

    def is_binary(self, file):

        parameters = ['file', '--mime', file]

        mime = subprocess.check_output(parameters, universal_newlines=True)
        match = re.search('charset=binary', mime)

        return match is not None

    def commit(self, path = '', identifier = 'author'):

        accumulator = Counter()

        for file in self.get_files(path):
            blame = self.blame(file)
            counter = self.process_blame(blame, identifier)

            accumulator = accumulator + counter

        print(self.presenter(accumulator))

    def process_blame(self, blame, identifier = 'author'):

        pattern = '^(?:{} )(.+)'.format(identifier)

        regex = re.compile(pattern, re.MULTILINE)
        matches = regex.findall(blame)

        return Counter(matches)

    def presenter(self, counter):

        sum_lines = sum(counter.values())

        blue = '\033[94m'
        grey = '\033[0m'
        endcolor = '\033[0m'
        italic = '\x1B[3m'
        eitalic = '\x1B[23m'

        template = '{0:>7.2%} {3}{2}{4}'
        top_n_contributors = 25

        if self.verbosity > 0:
            template = '{0:>7.2%} {3}{2}{4} ({1})'

        if self.verbosity > 1:
            top_n_contributors = None

        sorted_counter = reversed(counter.most_common(top_n_contributors))

        for author, contributions in sorted_counter:

            relative = float(contributions) / float(sum_lines)

            output = template.format(relative, contributions,
                                                  author, blue, endcolor,
                                                  italic, eitalic)

            print(output)
