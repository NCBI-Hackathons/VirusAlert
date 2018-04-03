#!/usr/bin/env python2

from docopt import docopt

def parse(args):
  top, bottom, left, right = margins(args['-m'])
  nrow, ncol = dimensions(args['-d'])
  return {
    'verbose' : args['-v'],
    'prefix'  : args['-p'],
    'top'     : top,
    'bottom'  : bottom,
    'left'    : left,
    'right'   : right,
    'side'    : pixels(args['-s']),
    'nchar'   : int(args['-n']),
    'nrow'    : nrow,
    'ncol'    : ncol,
    'pdfpath' : args['PDFPATH']
  }

def main():
  print parse(docopt(__doc__, version='longreadviruses 0.1'))

if __name__ == '__main__':
  main()
