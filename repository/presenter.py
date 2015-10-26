def out(counter, argv):

    sum_lines = sum(counter.values())

    blue = '\033[94m'
    grey = '\033[0m'
    endcolor = '\033[0m'
    italic = '\x1B[3m'
    eitalic = '\x1B[23m'

    template = '{0:>7.2%} {3}{2}{4}'

    if argv.show_absolute > 0:
        template = '{0:>7.2%} {3}{2}{4} ({1})'

    top_n = argv.top_n if argv.top_n > 0 else None

    sorted_counter = counter.most_common(top_n)

    if argv.alphabetically:
        sorted_counter = sorted(sorted_counter)

    if argv.reverse:
        sorted_counter = reversed(sorted_counter)

    for author, contributions in sorted_counter:

        relative = float(contributions) / float(sum_lines)

        output = template.format(relative, contributions, author, blue,
                                 endcolor, italic, eitalic)

        print(output)
