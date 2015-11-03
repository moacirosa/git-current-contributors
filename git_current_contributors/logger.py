import logging
import argv
import sys
import os

verbosity = (4 - argv.args.verbose) * 10

instance = logging.getLogger('git-current-contributors')
instance.setLevel(10)

formatter = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(verbosity)
stream_handler.setFormatter(formatter)

file_handler_output = '{}/.git/logs/current-contributors'.format(os.getcwd())
file_handler = logging.FileHandler(file_handler_output, 'w', delay=False)
file_handler.setLevel(10)
file_handler.setFormatter(formatter)

instance.addHandler(stream_handler)
instance.addHandler(file_handler)
