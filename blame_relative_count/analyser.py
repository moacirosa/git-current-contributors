import os
import re
import subprocess
import decorators
import time
from collections import Counter

def get_files(repository_path, argv):

    os.chdir(repository_path)

    parameters = ['git', 'ls-files', argv.path]
    files = subprocess.check_output(parameters, universal_newlines=True)

    return files.split()

@decorators.null_logger
def blame(repository_path, file, argv, logger=None):

    os.chdir(repository_path)

    if is_binary(file, logger) and not argv.force_binaries:
        logger.info('Skipping (binary) {} ...'.format(file))
        return ''

    logger.debug('Running over {} ...'.format(file))

    try:
        parameters = ['git', 'blame', '--line-porcelain', '-w', file]
        blame = subprocess.check_output(parameters, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logger.error(e)
        return ''

    return blame

@decorators.null_logger
def is_binary(file, logger=None):

    parameters = ['file', '--mime', file]

    try:
        mime = subprocess.check_output(parameters, universal_newlines=True)
        match = re.search('charset=binary', mime)
    except UnicodeDecodeError as e:
        logger.warning(file)
        logger.warning(e)
        match = True

    return match is not None

@decorators.null_logger
def commit(repository_path, argv, logger=None):

    start_time = time.time()
    accumulator = Counter()

    for file in get_files(repository_path, argv):
        porcelain_blame = blame(repository_path,  file, argv, logger)
        counter = process_blame(porcelain_blame, argv, logger)
        accumulator = accumulator + counter

    elapsed_time = time.time() - start_time

    logger.debug('Elapsed time {}'.format(elapsed_time))
    logger.debug('Final accumulator...')
    logger.debug(accumulator)

    return (accumulator, elapsed_time)

@decorators.null_logger
def process_blame(blame, argv, logger=None):

    pattern = '^(?:{} )(.+)'.format(argv.identifier)

    regex = re.compile(pattern, re.MULTILINE)
    matches = regex.findall(blame)
    counter = Counter(matches)

    logger.debug(counter)

    return counter
