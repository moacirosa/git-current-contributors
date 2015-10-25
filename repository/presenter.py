def out(counter, argv):

    sum_lines = sum(counter.values())

    blue = '\033[94m'
    grey = '\033[0m'
    endcolor = '\033[0m'
    italic = '\x1B[3m'
    eitalic = '\x1B[23m'

    template = '{0:>7.2%} {3}{2}{4}'
    top_n_contributors = 25

    if argv.verbose > 0:
        template = '{0:>7.2%} {3}{2}{4} ({1})'

    if argv.verbose > 1:
        top_n_contributors = None

    sorted_counter = counter.most_common(top_n_contributors)

    if argv.alphabetically:
        sorted_counter = sorted(sorted_counter)

    if argv.reverse:
        sorted_counter = reversed(sorted_counter)

    for author, contributions in sorted_counter:

        relative = float(contributions) / float(sum_lines)

        output = template.format(relative, contributions, author, blue,
                                 endcolor, italic, eitalic)

        print(output)
