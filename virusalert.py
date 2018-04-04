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

    # only fetch the first 10 entries in the fastq
    max_entries = 10

    v = VirLib()
    # fetch a fastq local path
    fastq_path = v.processInput(type='srr', input='SRR6172653')
    # return a list of BioPython objects representing each fastq entry in the file
    entries = v.entriesFromFastq(fastq=fastq_path)
    # BLAST, generate an XML, and parse to obtain the first species hit
    list_of_species = []
    for record in entries[:max_entries]:
        output_xml_path = v.blastAPISearch(record, output_xml_path='default.xml')
        species = v.fetchXMLResults(output_xml_path)
        list_of_species.append(species)

    # generate the output results in a file
    with open('species_results.txt', 'w') as f:
        print('Top hits by p-value in sample are: ')
        for s in list_of_species:
            f.write(s)
            f.write('\n')
            print(s)

if __name__ == '__main__':
    main()
