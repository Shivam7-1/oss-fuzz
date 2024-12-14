#!/bin/bash -eux

# Install dependencies from the test-requirements file
python3 -m pip install --no-cache-dir -r $SRC/visdom/test-requirements.txt

# Navigate to the Visdom project directory
cd $SRC/visdom

# Install the Visdom package
python3 setup.py install

# Copy the fuzzer script to the output directory
cp $SRC/visdom_fuzzer.py $OUT/visdom_fuzzer
