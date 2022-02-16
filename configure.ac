dnl Process this file with autoconf
AC_PREREQ([2.69])
AC_INIT(model-graph-neural-net, 0.1, franklin@bitsmasher.net, https://github.com/devsecfranklin/model-graph-neural-net)
AC_CONFIG_MACRO_DIR(cluster/m4)
AC_CONFIG_AUX_DIR(cluster)
dnl AC_CONFIG_HEADERS(config.h)
AM_INIT_AUTOMAKE

LT_INIT

AC_CONFIG_COMMANDS([franklin-build],
 [echo "(⊃｡•́‿•̀｡)⊃━⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿ Configuring for $mypkgname ☽༓･*˚⁺‧͙"],
 [mypkgname=$PACKAGE_NAME])
AM_PATH_PYTHON(3.8) # minimum version of Python
AC_CONFIG_FILES(cluster/Makefile) # Makefiles to generate, one per line
PY39="python$PYTHON_VERSION" # define the python interpreter
dnl LDFLAGS="$LDFLAGS -l$PY39"
AC_SUBST(PY39, python$PYTHON_VERSION)
AC_OUTPUT
