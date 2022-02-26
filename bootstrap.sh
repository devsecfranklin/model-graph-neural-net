#!/bin/bash

# 2/25/2022 Maintainer script 

# Author:  2730246+devsecfranklin@users.noreply.github.com 

# sudo apt install gnuplot gawk libtool psutils

if [ ! -f "./config.status" ]; then
  libtoolize
  aclocal -I aclocal/latex-m4/
  autoreconf -I aclocal/latex-m4/
  automake -a -c --add-missing
  ./configure
else
  ./config.status
fi

