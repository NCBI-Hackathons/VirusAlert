#!/usr/bin/env python3

from docopt import docopt
from virLib import VirLib
from Bio import SeqIO
from subprocess import check_call
# import os
from os.path import dirname, join, realpath

def datapath(path):
    return join(dirname(realpath(__file__)), 'data', path)

def toolpath(path):
    return join(dirname(realpath(__file__)), 'tools', path)

def parse(args):
    contdb = args['-d']
    if not contdb:
        contdb = datapath('viralg')
    return {
        'verbose' : args['-v'],
        'input'   : args['-i'],
        'cutoff'  : args['-c'],
        'contdb'  : contdb,
        'outdir'  : datapath(''),
        'intype'  : args['-t']
    }

def getinput(v, args):
    print(args)
    t = args['intype']
    if t == 'srr':
      i = v.processInput(type=t, input=args['input'])
      return i
    elif t == 'fastq':
      i = v.processInput(type=t, input=args['input'])
      SeqIO.convert(args['input'], "fastq", i, "fasta")
      return i
    elif t == 'fasta':
        return(args['input'])
    else:
        raise Exception('invalid intype: ' + t)

def magicblast(v, args):
    i = getinput(v, args)
    mb = toolpath('ncbi-magicblast-1.3.0/bin/magicblast')
    cmd = [mb, "-query",
            args['input'],
            "-db", args['contdb'],
            "-out", join(args['outdir'], "magicblast_hits.gz"),
            "-gzo -outfmt tabular"]
    print(cmd)
    check_call(cmd)

def virfinder(args):
    cmd = ["runVirFinder.R", args['input'], args['pvalue']]
    check_call(cmd)

# def virlib(args):

def main():
    with open('usage.txt', 'r') as f:
        args = parse(docopt(f.read(), version='virusalert 1.0'))
    v = VirLib(verbose=True)
    # print(args)
    # virfinder(args)
    magicblast(v, args)
    # virlib(args)
    # for i in args['input']:
    v.run(type=args['intype'], input=args['input'])

if __name__ == '__main__':
    main()
