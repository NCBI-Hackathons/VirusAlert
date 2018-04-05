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

def parseFastaHeaders(input_fasta):
    list_o_NC = []
    with open(input_fasta, 'r') as f:
        for line in f:
            if line.startswith('>'):
                line_parts = line.split('|')
                for i in line_parts:
                    if i.startswith('NC_'):
                        list_o_NC.append(i)
    return list_o_NC

def parse(v, args):
    contdb = args['-d']
    if not contdb:
        contdb = datapath('viralg')
    args = {
        'verbose' : args['-v'],
        'input'   : args['-i'],
        'cutoff'  : args['-c'],
        'contdb'  : contdb,
        'outdir'  : datapath(''),
        'intype'  : args['-t']
    }
    args = getinput(v, args)
    return args

def getinput(v, args):
    t = args['intype']
    if t == 'srr':
      i = v.processInput(type=t, input=args['input'])
      args['intype'] = 'fastq'
      args['input'] = i
      return args
    elif t == 'fastq':
      i = v.processInput(type=t, input=args['input'])
      SeqIO.convert(args['input'], "fastq", i, "fasta")
      args['intype'] = 'fasta'
      args['input'] = i
      return args
    elif t == 'fasta':
        return args
    else:
        raise Exception('invalid intype: ' + t)

def magicblast(v, args):
    mb = toolpath('ncbi-magicblast-1.3.0/bin/magicblast')
    cmd = [mb, "-query",
            args['input'],
            "-db", args['contdb'],
            "-out", join(args['outdir'], "magicblast_hits.gz"),
            "-infmt", args['intype'],
            "-gzo", "-outfmt", "tabular"]
    print(cmd)
    check_call(cmd)

def virfinder(args):
    cmd = ["../runVirFinder.R",
            '--vanilla',
            args['input'],
            args['cutoff']]
    check_call(cmd)

# def virlib(args):

def main():
    v = VirLib(verbose=True)
    with open('usage.txt', 'r') as f:
        args = parse(v, docopt(f.read(), version='virusalert 1.0'))
    print(args)
    magicblast(v, args)
    virfinder(args)
    # virlib(args)
    # for i in args['input']:
    # v.run(type=args['intype'], input=args['input'])

if __name__ == '__main__':
    main()
