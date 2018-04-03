#!/usr/bin/env python2

from docopt import docopt

def parse(args):
  return {
    'verbose' : args['-v'],
    'inputs'  : args['-i'],
    'outdir'  : args['-o'],
    'intype'  : args['-t'],
    'contdb'  : args['-c']
  }

def main():
  with open('usage.txt', 'r') as f:
    args = docopt(f.read(), version='longreadviruses 0.1')
  print parse(args)

if __name__ == '__main__':
  main()
