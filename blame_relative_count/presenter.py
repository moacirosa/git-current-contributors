import decorators
import datetime

def stdout(counter, elapsed_time, argv, logger=None):

    prepared_lines = prepare(counter, argv, elapsed_time, logger)
    output = '\n'.join(prepared_lines)

    print(output)

def csv(counter, argv, logger=None):

    sum_lines = sum(counter.values())
    sorted_counter = sorter(counter, argv)

    for author, contributions in sorted_counter:
        relative = float(contributions) / float(sum_lines)
        print('{}, {}, {}'.format(relative, contributions, author))

@decorators.null_logger
def prepare(counter, argv, elapsed_time = None, logger=None):

    blue = '\033[94m'
    grey = '\033[0m'
    endcolor = '\033[0m'
    italic = '\x1B[3m'
    eitalic = '\x1B[23m'

    template = '{0:>7.2%} {3}{2}{4}'

    if argv.show_absolute > 0:
        template = '{0:>7.2%} {3}{2}{4} ({1})'

    sum_lines = sum(counter.values())
    prepared_lines = []

    for author, contributions in sorter(counter, argv):

        relative = float(contributions) / float(sum_lines)

        output = template.format(relative, contributions, author, blue,
                                 endcolor, italic, eitalic)

        prepared_lines.append(output)

    top_n = check_top_n(counter, argv)
    n_contributors = 'Showing {}/{} contributors'.format(top_n, len(counter))
    elapsed ='Elapsed time: {}'.format(datetime.timedelta(seconds=elapsed_time))

    logger.info(n_contributors)
    logger.info(elapsed)

    prepared_lines.append('{}, {}'.format(n_contributors, elapsed))

    return prepared_lines

def sorter(counter, argv):

    top_n = check_top_n(counter, argv)
    sorted_counter = counter.most_common(top_n)

    if argv.alphabetically:
        sorted_counter = sorted(sorted_counter, key=lambda s: s[0].lower())

    if argv.reverse:
        sorted_counter = reversed(sorted_counter)

    return sorted_counter

def check_top_n(counter, argv):

    top_n = argv.top_n

    if top_n < 0 or top_n > len(counter):
        top_n = len(counter)

    return top_n
