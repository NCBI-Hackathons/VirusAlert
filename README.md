<img src="./images/virus-button.png" width="300">

# LongReadViruses

Discovery and validation of viruses using long read technology

Goal: To find viruses, both novel and known, in PacBio generated long read metagenomic data in order to find and diagnose viral infections in cultured cells using machine learning. 

Discovery and validation of viruses using VirFinder and RPS BLAST technology trainded with PacBio long read metagenomic data for PacBio long read metagenomic data. 

https://docs.google.com/presentation/d/125WTRdU_TjUtEwrDlG9p-orZDJxauGQl7ojDjvmwlMI/edit?usp=sharing

VirFinder
---------
 a novel k-mer based tool for identifying viral sequences from assembled metagenomic data

Install
-------

Run the top-level [install.sh][1] script.
It will install dependencies in the tools directory, and data files in the data directory.

Usage
-----

Run [longreadviruses.py][2]. See [usage.txt][3] for command line options.

[1]: install.sh
[2]: longreadviruses.py
[3]: usage.txt

Rough Plan
----------

git clone https://github.com/NCBI-Hackathons/LongReadViruses.git

#. Install (if not present) any BLAST dpeendencies, R, then VirFinder, and any pip dependencies (docopt).

::

    sh install.sh

#. Run program with sample options.

::

    python3 longreadviruses.py -d <database-path> -i <input-fasta-path> -o <output-results-directory-path>

This should:

::

    1. Fetch the fasta data from the SRR code.
    2. Run the fasta data with VirFinder.
    3. Programmatically BLAST to see what the top hits are.
    4. Return a graphic, a file of p-values, and a file of top hits in the output directory (date-stamped).
