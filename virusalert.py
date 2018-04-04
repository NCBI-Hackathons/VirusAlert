#!/usr/bin/env python3

from docopt import docopt
from virLib import VirLib

def parse(args):
    return {
        'verbose' : args['-v'],
        'inputs'  : args['-i'],
        'outdir'  : args['-o'],
        'intype'  : args['-t']
    }

def main():
    # with open('usage.txt', 'r') as f:
    #     args = docopt(f.read(), version='longreadviruses 0.1')
    # print(parse(args))

    v = VirLib()
    # requires srr code or fastq
    v.run(type='srr', input='SRR6172653', verbose=True)

if __name__ == '__main__':
    main()
