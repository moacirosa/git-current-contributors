import os
import re
import subprocess
import presenter
import logger
import time
from collections import Counter

def get_files(repository_path, argv):

    os.chdir(repository_path)

    parameters = ['git', 'ls-files', argv.path]
    files = subprocess.check_output(parameters, universal_newlines=True)

    return files.split()

def blame(repository_path, file, argv):

    os.chdir(repository_path)

    if is_binary(file) and not argv.force_binaries:
        logger.instance.info('Skipping (binary) {} ...'.format(file))
        return ''

    logger.instance.debug('Running over {} ...'.format(file))

    try:
        parameters = ['git', 'blame', '--line-porcelain', '-w', file]
        blame = subprocess.check_output(parameters, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logger.instance.error(e)
        return ''

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

    start_time = time.time()
    accumulator = Counter()

    for file in get_files(repository_path, argv):
        porcelain_blame = blame(repository_path,  file, argv)
        counter = process_blame(porcelain_blame, argv)
        accumulator = accumulator + counter

    elapsed_time = time.time() - start_time

    logger.instance.debug('Elapsed time {}'.format(elapsed_time))
    logger.instance.debug('Final accumulator...')
    logger.instance.debug(accumulator)

    return presenter.out(accumulator, argv, elapsed_time)

def process_blame(blame, argv):

    pattern = '^(?:{} )(.+)'.format(argv.identifier)

    regex = re.compile(pattern, re.MULTILINE)
    matches = regex.findall(blame)
    counter = Counter(matches)

    logger.instance.debug(counter)

    return counter
