# ForoyskPackage

ForoyskPackage is a Python package for processing and analyzing the Faroese language. It provides tools for word lookups, inflections, and more.

## Installation

You can install ForoyskPackage using pip:
# Clone the GitHub repository
git clone https://github.com/AnnikaSimonsen/foroyskt
cd foroyskt
# Install the package in editable mode
pip install -e .  # Note the dot!
cd src/foroyskt/resources
# Fetch the newest KRISTINsnid.csv.zip from Føroyski Bendingargrunnurin
wget -O KRISTINsnid.csv.zip https://urdarbrunnur.rhi.hi.is/bendingar-nidurhal/KRISTINsnid.csv.zip
# Unzip the data
unzip -q KRISTINsnid.csv.zip
rm KRISTINsnid.csv.*
cd ../../..
# Run the compressor to generate src/islenska/resources/compressed.bin
# You will get some Latin-1 encoding errors for certain lemmas
python tools/binpack.py
# Run the DAWG builder for the prefix and suffix files
python tools/dawgbuilder.py
# Now you're ready to go.
python FO_test.py
