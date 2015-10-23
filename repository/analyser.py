import os
import re
import subprocess
import presenter
import logger
from collections import Counter

def get_files(repository_path, subpath = ''):

    os.chdir(repository_path)

    parameters = ['git', 'ls-files', subpath]
    files = subprocess.check_output(parameters, universal_newlines=True)

    return files.split()

def blame(repository_path, file, skip_binary = True):

    os.chdir(repository_path)

    if is_binary(file) and skip_binary:
        logger.instance.info('Skipping (binary) {} ...'.format(file))
        return ''

    logger.instance.info('Running over {} ...'.format(file))

    parameters = ['git', 'blame', '--line-porcelain', '-w', file]
    blame = subprocess.check_output(parameters, universal_newlines=True)

    return blame

def is_binary(file):

    parameters = ['file', '--mime', file]

    mime = subprocess.check_output(parameters, universal_newlines=True)
    match = re.search('charset=binary', mime)

    return match is not None

def commit(repository_path, subpath = '', identifier = 'author', verbosity = 0):

    accumulator = Counter()

    for file in get_files(repository_path, subpath):
        porcelain_blame = blame(repository_path,  file, True)
        counter = process_blame(porcelain_blame, identifier)
        accumulator = accumulator + counter

    return presenter.out(accumulator, verbosity)

def process_blame(blame, identifier = 'author'):

    pattern = '^(?:{} )(.+)'.format(identifier)

    regex = re.compile(pattern, re.MULTILINE)
    matches = regex.findall(blame)

    return Counter(matches)
