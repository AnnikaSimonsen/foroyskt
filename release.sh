#!/bin/bash
# Build a BinPackage release and upload it to PyPi
if [ "$1" = "" ]; then
   echo "Version name argument missing"
   exit 1
fi
echo "Upload a new BinPackage version:" "$1"
# Fix permission bits
chmod -x src/foroyskt/*.py
chmod -x src/foroyskt/*.cpp
chmod -x src/foroyskt/resources/*
# Create the base source distribution
rm -rf build/*
python3 setup.py sdist
# Create the binary wheels
source wheels.sh
# Upload the new release
twine upload dist/foroyskt-$1*
echo "Upload of" "$1" "done"
