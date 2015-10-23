def out(counter, verbosity = 0):

    sum_lines = sum(counter.values())

    blue = '\033[94m'
    grey = '\033[0m'
    endcolor = '\033[0m'
    italic = '\x1B[3m'
    eitalic = '\x1B[23m'

    template = '{0:>7.2%} {3}{2}{4}'
    top_n_contributors = 25

    if verbosity > 0:
        template = '{0:>7.2%} {3}{2}{4} ({1})'

    if verbosity > 1:
        top_n_contributors = None

    sorted_counter = reversed(counter.most_common(top_n_contributors))

    for author, contributions in sorted_counter:

        relative = float(contributions) / float(sum_lines)

        output = template.format(relative, contributions, author, blue,
                                 endcolor, italic, eitalic)

        print(output)
