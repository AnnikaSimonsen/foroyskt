# Foroysk

Foroysk is a Python package for processing and analyzing the Faroese language. It provides tools for word lookups, inflections, and more. This is a fork of Miðeind's [BinPackage](https://github.com/mideind/BinPackage).

## Installation

You can install Foroysk using pip:

$ git clone https://github.com/AnnikaSimonsen/foroyskt

$ cd foroyskt

$ pip install -e .  # Note the dot!

$ cd src/foroyskt/resources

#wget -O KRISTINsnid.csv.zip https://urdarbrunnur.rhi.hi.is/bendingar-nidurhal/KRISTINsnid.csv.zip

Go into https://bendingar.fo/tilfar/ and get KRISTINsnid.csv.zip and put it into this folder!

$ unzip -q KRISTINsnid.csv.zip

$ rm KRISTINsnid.csv.*

$ cd ../../..

$ python tools/binpack.py

$ python tools/dawgbuilder.py

$ python FO_test.py

## Words missing from bendingar.fo

`src/foroyskt/resources/fo_additions.csv` holds Faroese words that are
missing from bendingar.fo. It is written by Annika Simonsen, in the same
format as `KRISTINsnid.csv`, and `tools/binpack.py` reads it right after
the bendingar.fo file. Word ids in it start at 900001, so they never clash
with bendingar.fo ids. Forms in it are checked by Annika.

## Contact

Annika Simonsen, ans72@hi.is
