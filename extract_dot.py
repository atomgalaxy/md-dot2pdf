#!/usr/bin/python

import sys
import argparse

def parse_args(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("input", type=argparse.FileType('r'))
    p.add_argument("--output", type=argparse.FileType('w'),
                   required=False, default=sys.stdout)
    p.add_argument("--chunk", type=int, default=0, required=False)
    p.add_argument("--invert", action="store_const", const=-1, required=False,
                   dest="chunk")
    return p.parse_args(argv)


def parse_file(in_file, out_file, chunk):
    current_chunk = 0
    in_chunk = False
    for line in in_file:
        if not in_chunk:
            if line.strip() == "```dot": # enter chunk
                in_chunk = True
            elif chunk == -1:
                out_file.write(line)
        else:
            if line.strip() == "```":    # finish chunk
                in_chunk = False
                current_chunk += 1
                continue
            elif current_chunk == chunk: # output line
                out_file.write(line)
                continue

def main(argv=None):
    args = parse_args(argv)
    parse_file(args.input, args.output, args.chunk)

if __name__ == "__main__":
    r = main()
    sys.exit(r if r is not None else 0)
