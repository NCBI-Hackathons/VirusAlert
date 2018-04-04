from __future__ import absolute_import
import unittest
import os
import zipfile
import shutil
import unittest
from virLib import VirLib

class VirusAlertTest(unittest.TestCase):
    """A set of test cases for toilwdl.py"""

    def setUp(self):
        """Stub init."""
        with open('input.fa', 'w') as f:
            f.write('test\n')
        with open('input.fq', 'w') as f:
            f.write('test\n')

    def tearDown(self):
        """Default tearDown for unittest."""
        if os.path.exists('input.fa'):
            os.unlink('input.fa')
        if os.path.exists('input.fq'):
            os.unlink('input.fq')
        if os.path.exists('default.xml'):
            os.unlink('default.xml')
        if os.path.exists('species_results.txt'):
            os.unlink('species_results.txt')

        srr_codes = ['SRR6172655', 'SRR6172653', 'SRR5383891', 'SRR5383888']
        for i in srr_codes:
            if os.path.exists(i + '.fastq'):
                os.unlink(i + '.fastq')
        unittest.TestCase.tearDown(self)

    def testBasicFasta(self):
        '''TESTING inputs with SRR fetching.'''
        v = VirLib(verbose=True)
        filepath = v.processInput(type='fasta', input='input.fa')
        assert filepath == os.path.abspath('input.fa')

    def testBasicFastq(self):
        '''TESTING inputs with SRR fetching.'''
        v = VirLib(verbose=True)
        filepath = v.processInput(type='fastq', input='input.fq')
        assert filepath == os.path.abspath('input.fq')

    def testBasicSRR(self):
        '''TESTING inputs with SRR fetching.'''
        v = VirLib(verbose=True)
        filepath = v.processInput(type='srr', input='SRR5150787')
        assert filepath == os.path.abspath('SRR5150787.fastq')

    def testRun(self):
        '''TESTING biopython BLAST API.'''
        v = VirLib(verbose=True)
        v.run(type='srr', input='SRR6172653')
        assert os.path.exists('species_results.txt')

    def testBatchSRR(self):
        '''TESTING Batch Fetching.'''
        v = VirLib(verbose=True)

        srr_codes = ['SRR6172655', 'SRR6172653', 'SRR5383891', 'SRR5383888']
        for i in srr_codes:
            filepath = v.processInput(type='srr', input=i)
            assert filepath == os.path.abspath(i + '.fastq')

    def testAccessionFetch(self):
        '''TESTING Fetching the Organism Name from a GenBank Accession #.'''
        v = VirLib(verbose=True)
        species = v.organismNamefromGenBankAccession('KY881787.1')
        assert 'Hepatitis B virus' in species

if __name__ == "__main__":
    unittest.main()  # run all tests