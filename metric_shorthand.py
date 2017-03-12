#!/usr/bin/env python3.6
prefixes = {24: ['yotta', 'Y'], 21: ['zetta', 'Z'], 18: ['exa', 'E'], 15: ['peta', 'P'],
            12: ['tera', 'T'], 9: ['giga', 'G'], 6: ['mega', 'M'], 3: ['kilo', 'k'],
            -3: ['milli', 'm'], -6: ['micro', 'µ'], -9: ['nano', 'n'], -12: ['pico', 'p'],
            -15: ['femto', 'f'], -18: ['atto', 'a'], -21: ['zepto', 'z'], -24: ['yocto', 'y']}
units = [['meter', 'm'], ['gram', 'g'], ['second', 's'],
         ['ampere', 'A'], ['kelvin', 'K'], ['mole', 'mol'], ['candela', 'cd'], ['liter', 'L']]
def shorthand(n, m):
    if m == 1:
        if n == -18:
            return (f'{m} {prefixes[n][0]}{unit[0]} (or {m} {prefixes[n][1]}{unit[1]}) should be called '
                    f'{m} {prefixes[n][0][:1]}{unit[1]} in shorthand.')
        else:
            return (f'{m} {prefixes[n][0]}{unit[0]} (or {m} {prefixes[n][1]}{unit[1]}) should be called '
                    f'{m} {prefixes[n][0][:2]}{unit[1]} in shorthand.')
    else:
        if n == -18:
            return (f'{m} {prefixes[n][0]}{unit[0]}s (or {m} {prefixes[n][1]}{unit[1]}) should be called '
                f'{m} {prefixes[n][0][:1]}{unit[1]}s in shorthand.')
        else:
            return (f'{m} {prefixes[n][0]}{unit[0]}s (or {m} {prefixes[n][1]}{unit[1]}) should be called '
                    f'{m} {prefixes[n][0][:2]}{unit[1]}s in shorthand.')
# picoseconds is hilarious
# do I wanna make nano 'nan'?
# might just have to come up with something special for amps
# attoseconds also hilarious
# exameters is weird
# picograms is pretty good as is nanograms
# there's no saving candelas
