import logging

def null_logger(func):

    def check_logger(*args):

        if type(args[-1]) is logging.Logger:
            return func(*args)

        null_logger = logging.getLogger('default-null-logger')

        args_list = list(args)
        args_list.pop()
        args_list.append(null_logger)

        return func(*args_list)

    return check_logger
