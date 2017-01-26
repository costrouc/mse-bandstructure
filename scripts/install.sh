#!/bin/bash

# Installs Quantum Espresso 6.0 in INSTALL_DIR.
# If installation fails it is most likely due to
# ./configure not working
# Needs to find FFT, BLAS, and LAPACK

LINK="http://qe-forge.org/gf/download/frsrelease/224/1044/"
FILENAME="qe-6.0"
EXTRACT_DIR="/tmp"
INSTALL_DIR=$HOME/.local/

wget -O $EXTRACT_DIR "$LINK/$FILENAME.tar.gz";
cd $EXTRACT_DIR;
tar -xzf $FILENAME.tar.gz;
cd $FILENAME;
./configure --prefix=$INSTALL_DIR;
make -j pw
make install
