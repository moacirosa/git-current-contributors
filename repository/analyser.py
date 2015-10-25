import os
import re
import subprocess
import presenter
import logger
from collections import Counter

def get_files(repository_path, argv):

    os.chdir(repository_path)

    parameters = ['git', 'ls-files', argv.path]
    files = subprocess.check_output(parameters, universal_newlines=True)

    return files.split()

def blame(repository_path, file, argv):

    skip_binary = True  # placeholder for new command setting
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

    try:
        mime = subprocess.check_output(parameters, universal_newlines=True)
        match = re.search('charset=binary', mime)
    except UnicodeDecodeError as e:
        logger.instance.warning(file)
        logger.instance.warning(e)
        match = True

    return match is not None

def commit(repository_path, argv):

    accumulator = Counter()

    for file in get_files(repository_path, argv):
        porcelain_blame = blame(repository_path,  file, True)
        counter = process_blame(porcelain_blame, argv)
        accumulator = accumulator + counter

    return presenter.out(accumulator, verbosity)

    return presenter.out(accumulator, argv)

def process_blame(blame, argv):

    pattern = '^(?:{} )(.+)'.format(argv.identifier)

    regex = re.compile(pattern, re.MULTILINE)
    matches = regex.findall(blame)
    counter = Counter(matches)

    logger.instance.info(counter)

    return counter
