#!/bin/bash

# 2/25/2022 Maintainer script 

# Author:  2730246+devsecfranklin@users.noreply.github.com 

# sudo apt install gnuplot gawk

libtoolize
aclocal -I aclocal/latex-m4/
autoreconf -I aclocal/latex-m4/
automake -a -c
./configure && ./config.status

