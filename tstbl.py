#!/usr/bin/env python3
# created_at: 2018-07-18 06:24:14 -0700
# remove w/: rm $HOME/scratch/python/Scratch_Gc1wQU.py

t0 = "15:13:12"
t1 = "21:04:33"

def sec_of_day(t):
    h, m, s = t.split(":")
    h, m, s = int(h), int(m), int(s)
    return s + m*60 + h*60*60

mults = [
    ("w", 60*60*24*7),
    ("d", 60*60*24),
    ("h", 60*60),
    ("m", 60),
    ("s", 1),
]

def fractional_representation(s):
    res = {"method": "frac",}
    for u, m in mults:
        res[u] = s / m
    return res
import math
def whole_representation(s):
    res = {"method": "whole",}
    for u, mult in mults:
        res[u] = max(math.floor(s/mult), 0)
        s -= res[u]*mult
    return res
def reps(s):
    return [
        fractional_representation(s),
        whole_representation(s),
    ]

H = ["method", "w", "d", "h", "m", "s"]
import tablib
def wide(R):
    ds = tablib.Dataset()
    ds.headers = H
    for r in R:
        ds.append([r[h] for h in ds.headers])
    print(ds)

def tall(R):
    ds2 = tablib.Dataset()
    ds2.headers = ["method", "frac", "whole"]
    
    for i, h in enumerate(H[1:]):
        row = [h]
        row.extend([r[h] for r in R])
        ds2.append(row)
        
    print(ds2)

import click
import click_completion
click_completion.init()

@click.command()
@click.argument('args', nargs=-1)
@click.option('--tall', 'display_mode', flag_value='tall', default=True)
@click.option('--wide', 'display_mode', flag_value='wide')
def time(args, display_mode):
    if len(args) == 1:
        delta = int(args[0])
    elif len(args) == 2:
        s0, s1 = map(sec_of_day, args)
        delta = max(s0, s1) - min(s0, s1)
    else:
        raise Exception("expect 1 or 2 args, got {}".format(len(args)))
    R = reps(delta)
    if display_mode == "wide":
        wide(R)
    elif display_mode == "tall":
        tall(R)
    

def main():
    time()

if __name__ == "__main__":
    main()
