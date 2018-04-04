import os
import subprocess
import requests

# BioPython
from Bio.Blast import NCBIWWW # NCBI API wrapper
from Bio.Blast import NCBIXML # parse output BLAST XML
from Bio import SeqIO # ingests fastas


# SRR5383888
# Human w/ HBV (PacBio): https://www.ncbi.nlm.nih.gov/sra/SRX2678953[accn]

# SRR5383891
# Human w/ HBV (PacBio; Control): https://www.ncbi.nlm.nih.gov/sra/SRX2678956[accn]

# SRR6172653
# PacBio Soil Samples: https://www.ncbi.nlm.nih.gov/sra/SRX3283433[accn]

# SRR6172655
# PacBio Soil Samples: https://www.ncbi.nlm.nih.gov/sra/SRX3283431[accn]


class VirLib(object):
    def __init__(self):
        self.SRA_tool_path = '/home/lifeisaboutfishtacos/Desktop/sratoolkit.2.9.0-ubuntu64/bin'
        self.fastq_dump_path = os.path.join(self.SRA_tool_path, 'fastq-dump')

    def process_inputs(self, type, input):
        """
        Returns the filepath to a local fasta file.

        Fetches fasta by SRR code if necessary.

        :param type:
        :param input:
        :return:
        """
        if type == 'fasta':
            assert (input.endswith('.fasta') or
                    input.endswith('.fa') or
                    input.endswith('.fastq') or
                    input.endswith('.fq'))
            return os.path.abspath(input)
        if type == 'srr':
            return self.get_srr_file(SRR_code=input)

    def get_srr_file(self, SRR_code):
        """
        Documentation: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=fastq-dump

        :param SRR_code:
        :return: filepath of downloaded fasta
        """
        # basic example cmd: "./fastq-dump -X 5 -Z SRR5150787"
        sratools_API_cmd = "{fastq_dump_path} -Z {SRR_code} > {SRR_code}.fastq" \
                           "".format(fastq_dump_path=self.fastq_dump_path,
                                     SRR_code=SRR_code)
        # run the command
        print('Now running: {cmd}'.format(cmd=sratools_API_cmd))
        process = subprocess.Popen(sratools_API_cmd, shell=True)
        process.communicate()
        # assert the output file was created and return
        SRR_filepath = os.path.join(os.getcwd(), SRR_code + '.fastq')
        assert os.path.exists(SRR_filepath)
        return os.path.join(SRR_filepath)

    def blast_API_search(self, fasta_path, output_xml_path= 'default.xml'):
        # process fasta as a biopython sequence record object
        record = SeqIO.read(fasta_path, format="fastq")
        result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)

        # save the output as an xml file
        with open(output_xml_path, "w") as out_handle:
            out_handle.write(result_handle.read())
        # self.fetch_XML_results(result_handle)

    def fetch_XML_results(self, output_xml_path):
        """
        Looks for the words 'virus or 'viral' in the xml headers and returns those that match.

        :param output_xml_path:
        :return:
        """
        matches = []
        accessions = []
        with open(output_xml_path, "r") as out_handle:
            blast_records = NCBIXML.parse(out_handle)
            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        accessions.append(self.get_accession(alignment.title))
                        # fetch the organism by the accession number instead
                        # possibly write if we care about the e value (hsp.expect)
                        if 'virus' in alignment.title or 'viral' in alignment.title:
                            matches.append(alignment.title)
        if matches:
            return matches
        else:
            return self.check_accessions(accessions)

    def get_accession(self, record):
        """"
        Given a SeqRecord, return the accession number as a string.

        e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "Z78488.1"
        """
        parts = record.id.split("|")
        assert len(parts) == 5 and parts[0] == "gi"
        return parts[3]

    def check_accessions(self):
        pass

    def print_XML_results(self, output_xml_path):
        """
        Only for debugging/verifying output.

        :param result_handle:
        :return:
        """
        # read the xml
        with open(output_xml_path, "r") as out_handle:
            blast_records = NCBIXML.parse(out_handle)
            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        print('****Alignment****')
                        print('sequence:', alignment.title)
                        print('length:', alignment.length)
                        print('e value:', hsp.expect)
                        print(hsp.query[0:75] + '...')
                        print(hsp.match[0:75] + '...')
                        print(hsp.sbjct[0:75] + '...')

# # TESTING inputs with SRR fetching
# v = VirLib()
# rv1 = v.process_inputs(type='fasta', input='input.fa')
# print(rv1)
# rv2 = v.process_inputs(type='srr', input='SRR5150787')
# print(rv2)

# TESTING biopython BLAST API
v = VirLib()
rv2 = v.process_inputs(type='srr', input='SRR5383888')
print(rv2)
v.blast_API_search(rv2, output_xml_path= 'default.xml')

# v = VirLib()
# x = ['SRR6172655', 'SRR6172653', 'SRR5383891', 'SRR5383888']
# for i in x:
#     v.process_inputs(type='srr', input=i)


# https://www.ncbi.nlm.nih.gov/nuccore/
response = requests.get('https://www.ncbi.nlm.nih.gov/nuccore/KY881787.1')
