#!/usr/bin/env python3

# Prints archive coverage by year and month

import pathlib
from collections import defaultdict, Counter
from calendar import monthrange, isleap


def scan(path):
    by_day = defaultdict(lambda: defaultdict(set))
    by_channel = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    path = pathlib.Path(path)
    channel_counts = defaultdict(int)
    total = 0
    for f in path.glob('**/*.txt'):
        c,y,m,d,*x = f.name.split('-')
        y = int(y, 10)
        m = int(m, 10)
        c = c.partition('(')[0]
        by_day[y][m].add(d)
        by_channel[y][m][c].add(d)
        channel_counts[c] += 1
        total += 1
    return by_day, by_channel, channel_counts, total


by_day, by_channel, channel_counts, total = scan('.')

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


print('')
print('Total days by Channel:')
channels = defaultdict(int)
for ky, y in by_channel.items():
    for km, m in y.items():
        for cy, c in m.items():
            channels[cy] += 1
print(sorted(channels.items(), key=lambda x: x[1], reverse=True))

print('')
print('Totals by Channel:')
print(sorted(channel_counts.items(), key=lambda x: x[1], reverse=True))

print('')
print('Total:', total)
