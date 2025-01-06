#!/usr/bin/env python3

# Prints archive coverage by year and month

import pathlib
from collections import defaultdict
from calendar import monthrange, isleap


def scan(path):
    by_day = defaultdict(lambda: defaultdict(set))
    by_channel = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    path = pathlib.Path(path)
    for f in path.glob('**/*.txt'):
        c,y,m,d,*x = f.name.split('-')
        y = int(y, 10)
        m = int(m, 10)
        c = c.partition('(')[0]
        by_day[y][m].add(d)
        by_channel[y][m][c].add(d)
    return by_day, by_channel


by_day, by_channel = scan('.')

print('Coverage by month:')
for ky, y in sorted(by_day.items()):
    days = days=366 if isleap(ky) else 365
    year_pct = 100 * sum(len(m) for m in y.values()) / days
    print(ky, '', ' '.join(f'{len(y[m]):2d}' for m in range(1, 13)), f'{year_pct:5.1f}%')

print('')
print('Months with complete coverage:')
for ky, y in sorted(by_day.items()):
    for km, m in sorted(y.items()):
        days = monthrange(ky, km)[1]
        if len(m) == days:
            print(f'{ky}-{km:02d} ', 'Total:', len(m), ' - ', '   '.join(f'{kc[:4]:>4s}: {len(c):2d}' for kc, c in sorted(by_channel[ky][km].items())))


