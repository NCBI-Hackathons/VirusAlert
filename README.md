LongReadViruses
===============

Discovery and validation of viruses using long read technology

Install
-------

Run the top-level [install.sh][1] script.
It will install dependencies in the tools directory,
and data files in the data directory.
Then use [run.sh][2] to run the analysis.

Biollante
---------

Run these in order to do the initial setup:

* [sequences/download_sequences.sh]()
* [DB/make_DB.sh]()

There are also a bunch of python scripts (33!). Not sure which are important.
Only `create_confusion_matrix.py` and
`create_plant_noncontaminated_training_pipeline.py` obviously work.

We'll move on for now and just use it for examples of `xgboost` probably.

VirusFriends
------------

* [setup.sh]() runs successfully
* Does it require EndoVir to actually run, or is it good?

[1]: install.sh
[2]: run.sh
