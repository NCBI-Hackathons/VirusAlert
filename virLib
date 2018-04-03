import os
import subprocess
import logging

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

        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            print(blast_record)


# # TESTING inputs with SRR fetching
# v = VirLib()
# rv1 = v.process_inputs(type='fasta', input='input.fa')
# print(rv1)
# rv2 = v.process_inputs(type='srr', input='SRR5150787')
# print(rv2)


# # TESTING biopython BLAST API
# v = VirLib()
# rv2 = v.process_inputs(type='srr', input='SRR5383888')
# print(rv2)
# v.blast_API_search(rv2, output_xml_path= 'default.xml')
