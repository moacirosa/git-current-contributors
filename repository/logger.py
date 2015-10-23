import logging
import argv
import sys

verbosity = (4 - argv.args.verbose) * 10

instance = logging.getLogger('git-current-contributors')
instance.setLevel(verbosity)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(verbosity)

instance.addHandler(stream_handler)
