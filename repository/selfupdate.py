import os
import logger
import subprocess

def update(repository_path):

    os.chdir(repository_path)
    output = subprocess.check_output(['git', 'pull', '--all'])

    for line in output.splitlines():
        logger.instance.debug(line)
