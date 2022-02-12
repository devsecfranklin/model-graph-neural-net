dnl Process this file with autoconf
AC_PREREQ([2.69])
AC_INIT(model-graph-neural-net, 0.1, franklin@bitsmasher.net)
AC_CONFIG_MACRO_DIR(cluster/m4)
AC_CONFIG_AUX_DIR(cluster)
AC_CONFIG_HEADERS(config.h)
AM_INIT_AUTOMAKE

AM_PATH_PYTHON(3.8) # minimum version of Python
AC_CONFIG_FILES(cluster/Makefile) # Makefiles to generate, one per line
PY39="python$PYTHON_VERSION" # define the python interpreter
LDFLAGS="$LDFLAGS -l$PY39"
AC_OUTPUT
