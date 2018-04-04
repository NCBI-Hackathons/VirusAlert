#!/usr/bin/env python3

from docopt import docopt
from virLib import VirLib

def parse(args):
    contdb = args['-d']
    if contdb is None:
        contdb = os.path.join(os.path.realpath(__file__), '../data/viralg')
    return {
        'verbose' : args['-v'],
        'input'   : args['-i'],
        'cutoff'  : args['-c'],
        'contdb'  : args['-d'],
        'outdir'  : args['-o'],
        'intype'  : args['-t']
    }

def contdb(args):
    if not args['contdb']:
        return

def virfinder(args):
    cmd = ["runVirFinder.R", args['input'], args['pvalue']]
    check_call(cmd)

def virlib(args):
    v = VirLib(verbose=True)
    for i in args['input']:
        v.run(type=args['intype'], input=i)

def main():
    with open('usage.txt', 'r') as f:
        args = docopt(f.read(), version='virusalert 1.0')
    virfinder(args)
    virlib(args)

if __name__ == '__main__':
    main()
